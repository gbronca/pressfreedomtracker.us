from django.test import TestCase

from incident.tests.factories import (
    IncidentPageFactory,
)

from incident.tests.utils import create_incident_filter


class ChoiceFilters(TestCase):
    def setUp(self):
        self.custody = 'CUSTODY'
        self.returned_full = 'RETURNED_FULL'
        self.unknown = 'UNKNOWN'

    def test_should_filter_by_choice_field(self):
        """should filter via a field that is a choice field"""

        target = IncidentPageFactory(
            status_of_seized_equipment=self.custody
        )
        IncidentPageFactory(
            status_of_seized_equipment=self.returned_full
        )
        summary, incidents = create_incident_filter(
            status_of_seized_equipment=self.custody
        ).fetch()

        self.assertEqual(len(incidents), 1)
        self.assertTrue(target in incidents)

    def test_filter_should_return_all_if_choice_field_invalid(self):
        """should not filter if choice is invalid"""

        IncidentPageFactory(
            status_of_seized_equipment=self.custody
        )
        IncidentPageFactory(
            status_of_seized_equipment=self.returned_full
        )
        IncidentPageFactory(
            affiliation='other'
        )
        summary, incidents = create_incident_filter(
            status_of_seized_equipment="hello"
        ).fetch()

        self.assertEqual(len(incidents), 3)

    def test_filter_should_handle_multiple_choices(self):
        """should handle multiple choices"""
        target1 = IncidentPageFactory(
            status_of_seized_equipment=self.custody
        )
        target2 = IncidentPageFactory(
            status_of_seized_equipment=self.returned_full
        )
        IncidentPageFactory(
            status_of_seized_equipment=self.unknown
        )

        summary, incidents = create_incident_filter(
            status_of_seized_equipment='{0},{1}'.format(self.custody, self.returned_full)
        ).fetch()

        self.assertEqual(len(incidents), 2)
        self.assertTrue(target1 in incidents)
        self.assertTrue(target2 in incidents)