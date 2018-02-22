from django.test import TestCase
from common.utils.fields import remove_unwanted_fields, get_field_tuple
from incident.models import IncidentPage


class TestRemoveUnwantedFields(TestCase):
    def test_returns_true_if_field_is_valid(self):
        included_field = IncidentPage._meta.get_field('arrest_status')
        self.assertTrue(remove_unwanted_fields(included_field))

    def test_returns_false_if_field_is_invalid(self):
        blacklisted_field = IncidentPage._meta.get_field('page_ptr')
        self.assertFalse(remove_unwanted_fields(blacklisted_field))

    def test_returns_false_if_inline_field_is_invalid(self):
        blacklisted_field = IncidentPage._meta.get_field('categories')
        self.assertFalse(remove_unwanted_fields(blacklisted_field))


class TestGetFieldTuple(TestCase):
    def test_field_with_verbose_name(self):
        field = IncidentPage._meta.get_field('arrest_status')
        expected = (field.name, field.verbose_name)
        self.assertEqual(
            get_field_tuple(field),
            expected
        )

    def test_field_without_verbose_name(self):
        field = IncidentPage._meta.get_field('city')
        expected = (field.name, field.name)
        self.assertEqual(
            get_field_tuple(field),
            expected
        )

    def test_inline_field(self):
        field = IncidentPage._meta.get_field('equipment_seized')
        expected = (field.name, field.related_model._meta.verbose_name)
        self.assertEqual(
            get_field_tuple(field),
            expected
        )
