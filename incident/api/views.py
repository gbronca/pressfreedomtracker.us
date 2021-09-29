import collections
from typing import TYPE_CHECKING

from rest_framework import viewsets
from rest_framework.settings import api_settings
from rest_framework.pagination import CursorPagination
from rest_framework.response import Response
from rest_framework.utils.urls import remove_query_param
from rest_framework_csv.renderers import PaginatedCSVRenderer

from incident.api.serializers import (
    IncidentSerializer,
    ItemSerializer,
    EquipmentSerializer,
    FlatIncidentSerializer,
)
from incident import models
from incident.utils.incident_filter import IncidentFilter

if TYPE_CHECKING:
    from django.http import HttpResponse


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

    def dispatch(self, *args, **kwargs) -> 'HttpResponse':
        response = super().dispatch(*args, **kwargs)

        # Allow requests from any orign to allow this to be an accessible API
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'GET,OPTIONS,HEAD'

        return response

    def get_renderer_context(self):
        context = super().get_renderer_context()

        # Get set of fields from serializer that has been pruned
        # according to request's query-string parameters.
        context['header'] = list(self.get_serializer().fields.keys())
        return context

    def get_serializer_class(self):
        if self.request.accepted_renderer.format == 'csv':
            return FlatIncidentSerializer
        return super().get_serializer_class()

    def paginate_queryset(self, queryset):
        if self.request.accepted_renderer.format == 'csv':
            return None
        return super().paginate_queryset(queryset)

    def get_queryset(self):
        incident_filter = IncidentFilter(self.request.GET)
        incidents = incident_filter.get_queryset()

        return incidents.with_most_recent_update().with_public_associations()


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
