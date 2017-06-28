from django.db import models

from modelcluster.contrib.taggit import ClusterTaggableManager


EXCLUDED_FIELDS = (
    'id',
    'has_unpublished_changes',
    'live',
    'locked',
    'numchild',
    'path',
    'page_ptr',
    'url_path',
    'revisions',
    'related_incidents',  # not sure how to represent this in export
    'group_permissions',
    'depth',
    'content_type',
    'formsubmission',
    'go_live_at',
    'view_restrictions',
    'redirect',
)


def humanize(obj):
    """Attempt to make a flat, human-readable representation of an object"""
    if hasattr(obj, 'summary'):
        return obj.summary
    else:
        return str(obj)


def is_exportable(field):
    """Return True if a data field should be exported"""
    name = field.name
    return not (name.startswith('tagged_') or name in EXCLUDED_FIELDS)


def to_row(obj):
    """Flatten a model object into a list of strings suitable for a CSV

    This function attempts to introspect an object's fields and turn
    each value into a string that could appear in a CSV export.  This
    will follow ForeignKey or ManyToMany relationships and represent
    those values as comma-delimited strings with some representation
    of the objects on the other end of the relationship.

    """
    row = []

    model = type(obj)
    model_fields = model._meta.get_fields()

    for field in filter(is_exportable, model_fields):
        if type(field) == models.ForeignKey:
            val = getattr(obj, field.name)
            if val:
                val = str(val)
        elif type(field) in (models.ManyToManyField, models.ManyToOneRel, ClusterTaggableManager):
            val = u', '.join(
                [humanize(item) for item in getattr(obj, field.name).all()]
            )
        elif hasattr(field, 'choices') and field.choices:
            val = getattr(obj, 'get_%s_display' % field.name)()
        elif hasattr(obj, field.name):
            val = getattr(obj, field.name)
        row.append(str(val))
    return row
