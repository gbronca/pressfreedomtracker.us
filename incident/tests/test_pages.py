from wagtail.wagtailcore.models import Site
from django.test import TestCase, Client

from incident.models.incident_page import IncidentPage
from incident.models.export import is_exportable, to_row
from .factories import IncidentIndexPageFactory, IncidentPageFactory


class TestPages(TestCase):
    def setUp(self):
        self.client = Client()

        site = Site.objects.get()
        self.index = IncidentIndexPageFactory(
            parent=site.root_page, slug='incidents')

    def test_get_index_should_succeed(self):
        response = self.client.get('/incidents/')
        self.assertEqual(response.status_code, 200)

    def test_get_index_should_succeed_with_filters(self):
        response = self.client.get(
            '/incidents/?search=text&upper_date=2017-01-01&categories=1,2'
        )
        self.assertEqual(response.status_code, 200)

    def test_get_index_should_succeed_with_malformed_filters(self):
        response = self.client.get(
            '/incidents/?upper_date=aaa&lower_date=2011-54-39'
        )
        self.assertEqual(response.status_code, 200)


class TestExportPage(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()

        site = Site.objects.get()
        cls.index = IncidentIndexPageFactory(
            parent=site.root_page, slug='incidents')

    def test_export_should_succeed(self):
        response = self.client.get(
            '/incidents/export/'
        )
        self.assertEqual(response.status_code, 200)

    def test_export_should_include_headers(self):
        response = self.client.get(
            '/incidents/export/'
        )
        content_lines = list(response.streaming_content)
        expected_headers = [
            field.name for field in IncidentPage._meta.get_fields()
            if is_exportable(field)
        ]
        self.assertEqual(
            content_lines[0].decode('utf-8'),
            ','.join(expected_headers) + '\r\n',
        )

    def test_export_should_include_incidents_only_live_incidents(self):
        inc = IncidentPageFactory(title='Live incident')
        IncidentPageFactory(title='Unpublished incident', live=False)
        response = self.client.get(
            '/incidents/export/'
        )

        content_lines = list(response.streaming_content)
        self.assertEqual(
            ','.join(to_row(inc)) + '\r\n',
            content_lines[1].decode('utf-8'),
        )
        for line in content_lines:
            self.assertNotIn('Unpublished incident', line.decode('utf-8'))