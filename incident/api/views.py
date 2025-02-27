import collections
from typing import TYPE_CHECKING

from django.contrib.postgres.aggregates import StringAgg
from django.core.exceptions import ValidationError
from django.db.models import (
    CharField,
    OuterRef,
    Subquery,
)
from rest_framework.decorators import action
from drf_spectacular.utils import (
    extend_schema,
    OpenApiParameter,
)
from rest_framework import viewsets, status
from rest_framework.settings import api_settings
from rest_framework.pagination import CursorPagination
from rest_framework.response import Response
from rest_framework.utils.urls import remove_query_param
from rest_framework_csv.renderers import PaginatedCSVRenderer, CSVRenderer

from common.models import CategoryPage
from incident.api.serializers import (
    IncidentSerializer,
    ItemSerializer,
    EquipmentSerializer,
    CategorySerializer,
    FlatIncidentSerializer,
)
from incident import models
from incident.utils.incident_filter import IncidentFilter, get_openapi_parameters, DateFilter

if TYPE_CHECKING:
    from django.http import HttpResponse


class HomePageCSVRenderer(CSVRenderer):
    header = ['date', 'city', 'state__abbreviation', 'latitude', 'longitude', 'category_summary', 'tag_summary']
    labels = {
        'state__abbreviation': 'state',
        'category_summary': 'categories',
        'tag_summary': 'tags',
    }


class HeaderCursorPagination(CursorPagination):
    def get_first_link(self):
        url = self.request.build_absolute_uri()
        return remove_query_param(url, self.cursor_query_param)

    def paginate_queryset(self, queryset, request, view=None):
        self.use_envelope = False
        self.request = request
        if str(request.GET.get('envelope')).lower() == '1':
            self.use_envelope = True
        return super().paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        next_url = self.get_next_link()
        previous_url = self.get_previous_link()
        first_url = self.get_first_link()

        links = []
        for url, label in (
                (first_url, 'first'),
                (previous_url, 'prev'),
                (next_url, 'next'),
        ):
            if url is not None:
                links.append('<{}>; rel="{}"'.format(url, label))
        headers = {'Link': ', '.join(links)} if links else {}

        if self.use_envelope:
            return Response(collections.OrderedDict([
                ('first', first_url),
                ('next', next_url),
                ('previous', previous_url),
                ('results', data)
            ]), headers=headers)
        return Response(data, headers=headers)


class IncidentCursorPagination(HeaderCursorPagination):
    page_size = 25
    page_size_query_param = 'limit'
    ordering = '-unique_date'


class IncidentViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = IncidentSerializer
    renderer_classes = tuple(api_settings.DEFAULT_RENDERER_CLASSES) + (PaginatedCSVRenderer,)
    pagination_class = IncidentCursorPagination

    @extend_schema(
        parameters=get_openapi_parameters() + [
            OpenApiParameter(
                name='fields',
                type={
                    'type': 'array',
                    'items': {
                        'type': 'string',
                        'enum': list(IncidentSerializer().fields),
                    }
                },
                location=OpenApiParameter.QUERY,
                required=False,
                description='Specify which incident fields are given on the result data.',
                style='form',
                explode=False,
            )
        ]
    )
    def list(self, *args, **kwargs):
        return super().list(*args, **kwargs)

    def dispatch(self, *args, **kwargs) -> 'HttpResponse':
        response = super().dispatch(*args, **kwargs)

        # Allow requests from any orign to allow this to be an accessible API
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'GET,OPTIONS,HEAD'

        return response

    def get_renderer_context(self):
        context = super().get_renderer_context()

        # Get set of fields from serializer that has been pruned
        # according to request's query-string parameters.  In the
        # homepage_csv action, this set is pre-determined and not
        # affected by the request, in that case we skip this step.
        if self.action != 'homepage_csv':
            context['header'] = list(self.get_serializer().fields.keys())
        return context

    def get_serializer_class(self):
        if getattr(self.request, 'accepted_renderer', None) and self.request.accepted_renderer.format == 'csv':
            return FlatIncidentSerializer
        return super().get_serializer_class()

    def paginate_queryset(self, queryset):
        if getattr(self.request, 'accepted_renderer', None) and self.request.accepted_renderer.format == 'csv':
            return None
        return super().paginate_queryset(queryset)

    def get_queryset(self):
        incident_filter = IncidentFilter(self.request.GET)
        incidents = incident_filter.get_queryset()

        return incidents.with_most_recent_update().with_public_associations()

    @action(detail=False, renderer_classes=[HomePageCSVRenderer], url_name='homepage_csv')
    def homepage_csv(self, request, version=None):
        date_filter = DateFilter(
            'date',
            models.IncidentPage._meta.get_field('date'),
            fuzzy=True,
        )
        value = date_filter.get_value(request.GET)
        try:
            cleaned_value = date_filter.clean(value, strict=True)
        except ValidationError:
            return Response([], status=status.HTTP_400_BAD_REQUEST)

        tag_summary = models.IncidentPage.objects.only('tags').annotate(
            tag_summary=StringAgg(
                'tags__title',
                delimiter=', ',
                ordering=('tags__title',)
            )
        ).filter(pk=OuterRef('pk'))
        category_summary = models.IncidentPage.objects.only('categories').annotate(
            category_summary=StringAgg(
                'categories__category__title',
                delimiter=', ',
                ordering=('categories__category__title',)
            )
        ).filter(pk=OuterRef('pk'))

        incidents = models.IncidentPage.objects.live().only('date', 'city', 'state', 'latitude', 'longitude').annotate(
            tag_summary=Subquery(tag_summary.values('tag_summary'), output_field=CharField()),
            category_summary=Subquery(category_summary.values('category_summary'), output_field=CharField()),
        )
        if cleaned_value is not None:
            incidents = date_filter.filter(incidents, cleaned_value)

        incidents = incidents.values(
            'date', 'city', 'state__abbreviation', 'latitude', 'longitude', 'category_summary', 'tag_summary'
        )

        incidents = list(incidents)  # CSV Renderer requires a list
        return Response(incidents)


class JournalistViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Journalist.objects.all()
    serializer_class = ItemSerializer


class InstitutionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Institution.objects.all()
    serializer_class = ItemSerializer


class GovernmentWorkerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.GovernmentWorker.objects.all()
    serializer_class = ItemSerializer


class ChargeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Charge.objects.all()
    serializer_class = ItemSerializer


class NationalityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Nationality.objects.all()
    serializer_class = ItemSerializer


class PoliticianOrPublicViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.PoliticianOrPublic.objects.all()
    serializer_class = ItemSerializer


class VenueViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Venue.objects.all()
    serializer_class = ItemSerializer


class EquipmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Equipment.objects.all()
    serializer_class = EquipmentSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CategoryPage.objects.all()
    serializer_class = CategorySerializer
