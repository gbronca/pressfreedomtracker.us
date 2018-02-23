from datetime import date
import copy

from django.core.exceptions import ValidationError
from django.db.models import (
    BooleanField,
    CharField,
    Count,
    DateField,
    DurationField,
    F,
    ForeignKey,
    ManyToManyField,
    Q,
    TextField,
    Value,
)
from django.db.models.functions import Trunc, Cast
from django.db.models.fields.related import ManyToOneRel
from psycopg2.extras import DateRange
from wagtail.wagtailcore.fields import RichTextField, StreamField

from incident.circuits import STATES_BY_CIRCUIT
from incident.utils.db import MakeDateRange


class Filter(object):
    serialized_type = 'text'

    def __init__(self, name, model_field, lookup=None):
        self.name = name
        self.model_field = model_field
        self.lookup = lookup or name

    def __repr__(self):
        return '<{}: {}>'.format(
            self.__class__.__name__,
            self.name,
        )

    def get_value(self, data):
        return data.get(self.name) or None

    def clean(self, value, strict=False):
        return self.model_field.to_python(value)

    def get_allowed_parameters(self):
        return {self.name}

    def filter(self, queryset, value):
        """
        Filter the queryset according to the given (cleaned) value.

        This will only get called if value is not None.
        """
        return queryset.filter(**{self.lookup: value})

    def get_verbose_name(self):
        return self.model_field.verbose_name

    def serialize(self):
        serialized = {
            'title': self.get_verbose_name(),
            'type': self.serialized_type,
            'name': self.name,
        }
        return serialized


class BooleanFilter(Filter):
    serialized_type = 'bool'


class RelationFilter(Filter):
    serialized_type = 'autocomplete'


class DateFilter(Filter):
    serialized_type = 'date'

    def __init__(self, name, model_field, lookup=None, fuzzy=False):
        self.fuzzy = fuzzy
        super(DateFilter, self).__init__(name, model_field, lookup=lookup)

    def get_value(self, data):
        start = data.get('{}_lower'.format(self.name)) or None
        end = data.get('{}_upper'.format(self.name)) or None
        return start, end

    def clean(self, value, strict=False):
        start, end = value

        start = self.model_field.to_python(start)
        end = self.model_field.to_python(end)

        if start and end and start > end:
            value = None
            if strict:
                raise ValidationError('{}_lower must be less than or equal to {}_upper'.format(
                    self.name,
                    self.name,
                ))
        elif start or end:
            value = (start, end)
        else:
            # No error raised here because 'no value' is okay.
            value = None

        return value

    def get_allowed_parameters(self):
        return {'{}_lower'.format(self.name), '{}_upper'.format(self.name)}

    def filter(self, queryset, value):
        lower_date, upper_date = value

        if lower_date == upper_date:
            return queryset.filter(**{self.lookup: lower_date})

        if self.fuzzy:
            queryset = queryset.annotate(
                fuzzy_date=MakeDateRange(
                    Cast(Trunc('date', 'month'), DateField()),
                    Cast(F('date') + Cast(Value('1 month'), DurationField()), DateField()),
                ),
            )
            target_range = DateRange(
                lower=lower_date,
                upper=upper_date,
                bounds='[]'
            )
            exact_date_match = Q(
                date__contained_by=target_range,
                exact_date_unknown=False,
            )

            inexact_date_match_lower = Q(
                exact_date_unknown=True,
                fuzzy_date__overlap=target_range,
            )

            return queryset.filter(exact_date_match | inexact_date_match_lower)

        return queryset.filter(**{
            '{0}__contained_by'.format(self.lookup): DateRange(
                lower=lower_date,
                upper=upper_date,
                bounds='[]'
            )
        })


class ChoiceFilter(Filter):
    @property
    def serialized_type(self):
        choices = self.get_choices()
        if 'JUST_TRUE' in choices:
            return 'radio'
        return 'choice'

    def get_choices(self):
        return {choice[0] for choice in self.model_field.choices}

    def clean(self, value, strict=False):
        if not value:
            return None
        values = value.split(',')
        value = []
        invalid_values = []
        choices = self.get_choices()

        for v in values:
            if v in choices:
                value.append(v)
            else:
                invalid_values.append(v)

        if invalid_values and strict:
            raise ValidationError('Invalid value{} for {}: {}'.format(
                's' if len(invalid_values) != 1 else '',
                self.name,
                ','.join(invalid_values),
            ))
        return value or None

    def filter(self, queryset, value):
        return queryset.filter(**{'{}__in'.format(self.lookup): value})


class ManyRelationFilter(Filter):
    serialized_type = 'autocomplete'

    def clean(self, value, strict=False):
        if not value:
            return None
        values = value.split(',')
        invalid_values = []

        value = []
        for v in values:
            try:
                value.append(int(v))
            except ValueError:
                invalid_values.append(v)

        if invalid_values and strict:
            raise ValidationError('Invalid value{} for {}: {}'.format(
                's' if len(invalid_values) != 1 else '',
                self.name,
                ','.join(invalid_values),
            ))
        return value

    def filter(self, queryset, value):
        return queryset.filter(**{'{}__in'.format(self.lookup): value})

    def get_verbose_name(self):
        if hasattr(self.model_field, 'verbose_name'):
            return self.model_field.verbose_name
        return self.model_field.related_model._meta.verbose_name

    def serialize(self):
        serialized = super(ManyRelationFilter, self).serialize()
        related_model = self.model_field.remote_field.model
        if isinstance(self.model_field, ManyToOneRel) and hasattr(related_model, '_autocomplete_model'):
            serialized['autocomplete_type'] = related_model._autocomplete_model
        else:
            serialized['autocomplete_type'] = 'incident.{}'.format(related_model.__name__)
        return serialized


class SearchFilter(Filter):
    def __init__(self):
        super(SearchFilter, self).__init__('search', CharField())

    def filter(self, queryset, value):
        return queryset.search(value, order_by_relevance=False)


class ChargesFilter(ManyRelationFilter):
    def filter(self, queryset, value):
        dropped_charges_match = Q(dropped_charges__in=value)
        current_charges_match = Q(current_charges__in=value)
        return queryset.filter(current_charges_match | dropped_charges_match)

    def serialize(self):
        serialized = super(ManyRelationFilter, self).serialize()
        serialized['autocomplete_type'] = 'incident.Charge'
        return serialized


class CircuitsFilter(ChoiceFilter):
    def get_choices(self):
        return set(STATES_BY_CIRCUIT)

    def filter(self, queryset, value):
        states = set()
        for circuit in value:
            states |= set(STATES_BY_CIRCUIT[circuit])

        return queryset.filter(state__name__in=states)


def get_category_options():
    from common.models import CategoryPage
    available_filters = IncidentFilter.get_available_filters()
    return [
        {
            'id': page.id,
            'title': page.title,
            'url': page.url,
            'related_fields': [
                available_filters[obj.incident_filter].serialize()
                for obj in page.incident_filters.all()
                if obj.incident_filter in available_filters
            ],
        }
        for page in CategoryPage.objects.live().prefetch_related('incident_filters')
    ]


class IncidentFilter(object):
    base_filters = {
        'affiliation',
        'categories',
        'circuits',
        'city',
        'date',
        'state',
        'tags',
        'targets',
        'lawsuit_name',
        'venue',
    }

    filter_overrides = {
        'date': {'fuzzy': True},
        'equipment_seized': {'lookup': 'equipment_seized__equipment'},
        'equipment_broken': {'lookup': 'equipment_broken__equipment'},
        'categories': {'lookup': 'categories__category'},
    }

    _extra_filters = {
        'circuits': CircuitsFilter(name='circuits', model_field=CharField()),
        'charges': ChargesFilter(name='charges', model_field=CharField()),
    }

    # IncidentPage fields that cannot be filtered on.
    # RichTextFields, TextFields, and StreamFields can never be filtered on,
    # regardless of whether they're in this list or not.
    exclude_fields = {
        'page_ptr',
        'exact_date_unknown',
        'teaser_image',
        'related_incidents',
        'updates',
        'search_image',
    }

    def __init__(self, data):
        self.data = data
        self.cleaned_data = None
        self.errors = None
        self.search_filter = None
        self.filters = None

    @classmethod
    def get_available_filters(cls):
        """
        Returns a dictionary mapping filter names to filter instances.
        """
        # Prevent circular imports
        from incident.models.incident_page import IncidentPage

        filters = copy.deepcopy(cls._extra_filters)

        fields = IncidentPage._meta.get_fields(include_parents=False)
        for field in fields:
            if isinstance(field, (RichTextField, StreamField, TextField)):
                continue
            if field.name in cls.exclude_fields:
                continue
            filters[field.name] = cls._get_filter(field)

        return filters

    @classmethod
    def get_filter_choices(cls):
        return FilterChoicesIterator()

    @classmethod
    def _get_filter(cls, model_field):
        kwargs = {
            'filter_cls': Filter,
            'name': model_field.name,
            'model_field': model_field,
        }

        if isinstance(model_field, (ManyToManyField, ManyToOneRel)):
            kwargs['filter_cls'] = ManyRelationFilter
        elif isinstance(model_field, ForeignKey):
            kwargs['filter_cls'] = RelationFilter
        elif isinstance(model_field, DateField):
            kwargs['filter_cls'] = DateFilter
        elif model_field.choices:
            kwargs['filter_cls'] = ChoiceFilter
        elif isinstance(model_field, BooleanField):
            kwargs['filter_cls'] = BooleanFilter

        if model_field.name in cls.filter_overrides:
            kwargs.update(cls.filter_overrides[model_field.name])

        filter_cls = kwargs.pop('filter_cls')
        return filter_cls(**kwargs)

    def clean(self, strict=False):
        from common.models import CategoryPage
        self.cleaned_data = {}
        errors = []

        self.search_filter = SearchFilter()

        available_filters = IncidentFilter.get_available_filters()
        self.filters = [available_filters[name] for name in self.base_filters]

        for f in [self.search_filter] + self.filters:
            try:
                cleaned_value = f.clean(f.get_value(self.data), strict=strict)
                if cleaned_value is not None:
                    self.cleaned_data[f.name] = cleaned_value
            except ValidationError as exc:
                errors.extend(exc.error_list)

        category_ids = self.cleaned_data.get('categories')
        if category_ids:
            categories = CategoryPage.objects.live().filter(
                id__in=category_ids,
            ).prefetch_related(
                'incident_filters',
            )
            category_filters = [
                available_filters[obj.incident_filter]
                for category in categories
                for obj in category.incident_filters.all()
                if obj.incident_filter in available_filters
            ]
            self.filters += category_filters
            for f in category_filters:
                try:
                    value = f.get_value(self.data)
                    if value is not None:
                        cleaned_value = f.clean(value, strict=strict)
                        if cleaned_value is not None:
                            self.cleaned_data[f.name] = cleaned_value
                except ValidationError as exc:
                    errors.append(str(exc))

        if strict:
            allowed_parameters = self.search_filter.get_allowed_parameters()
            for f in self.filters:
                allowed_parameters |= f.get_allowed_parameters()
            invalid_parameters = set(self.data) - allowed_parameters
            if invalid_parameters:
                errors.append(['Invalid parameter{} provided: {}'.format(
                    's' if len(invalid_parameters) != 1 else '',
                    ','.join(invalid_parameters),
                )])

            if errors:
                raise ValidationError(errors)

    def _get_queryset(self):
        # Prevent circular imports
        from incident.models.incident_page import IncidentPage
        if self.cleaned_data is None:
            self.clean()

        queryset = IncidentPage.objects.live()

        for f in self.filters:
            cleaned_value = self.cleaned_data.get(f.name)
            if cleaned_value is not None:
                queryset = f.filter(queryset, cleaned_value)

        return queryset.distinct()

    def get_queryset(self):
        queryset = self._get_queryset().order_by('-date', 'path').distinct()

        search = self.cleaned_data.get('search')
        if search:
            queryset = self.search_filter.filter(queryset, search)

        return queryset

    def get_summary(self):
        """
        Return a tuple of (label, value) pairs with summary data of the
        incidents.

        The data this chooses to summarize is based on the presence and value
        of particular filters.

        """
        from common.models import CategoryPage
        queryset = self._get_queryset()

        TODAY = date.today()
        THIS_YEAR = TODAY.year
        THIS_MONTH = TODAY.month

        summary = (
            ('Total Results', queryset.count()),
        )

        # Add counts for this year and this month if non-zero
        incidents_this_year = queryset.filter(date__contained_by=DateRange(
            TODAY.replace(month=1, day=1),
            TODAY.replace(month=12, day=31),
            bounds='[]'
        ))

        # Only increment month if there's another month in the year.
        if THIS_MONTH < 12:
            next_month = THIS_MONTH + 1
        else:
            next_month = THIS_MONTH

        incidents_this_month = queryset.filter(date__contained_by=DateRange(
            TODAY.replace(day=1),
            TODAY.replace(month=next_month, day=1),
            bounds='[)'
        ))

        search = self.cleaned_data.get('search')
        if search:
            incidents_this_year = self.search_filter.filter(incidents_this_year, search)
            incidents_this_month = self.search_filter.filter(incidents_this_month, search)
        num_this_year = incidents_this_year.count()
        num_this_month = incidents_this_month.count()

        if num_this_year > 0:
            summary = summary + ((
                'Results in {}'.format(THIS_YEAR),
                num_this_year
            ),)

        if num_this_month > 0:
            summary = summary + ((
                'Results in {0:%B}'.format(TODAY),
                num_this_month
            ),)

        # If more than one category is included in this set, add a summary item
        # for each category of the form ("Total <Category Name>", <Count>)
        category_pks = self.cleaned_data.get('categories')
        if category_pks:
            categories = CategoryPage.objects.filter(
                pk__in=category_pks
            ).annotate(num_incidents=Count('incidents'))
            for category in categories:
                summary = summary + ((
                    category.plural_name if category.plural_name else category.title,
                    category.num_incidents,
                ),)

        return summary


class FilterChoicesIterator(object):
    """
    Helper class to get around circular imports.
    """
    def __iter__(self):
        for name, filter_ in IncidentFilter.get_available_filters().items():
            if name == 'search' or name in IncidentFilter.base_filters:
                continue
            yield (name, filter_.get_verbose_name())
