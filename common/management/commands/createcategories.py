from django.core.management.base import BaseCommand

from django.db import transaction

from wagtail.core.models import Page

from common.models import CategoryPage
from common.tests.factories import (
    CategoryPageFactory,
    DevelopmentSiteFactory,
)
from home.tests.factories import StatBoxFactory, HomePageFactory


CATEGORIES = {
    'arrest': [
        'arrest_status',
        'status_of_charges',
        'detention_date',
        'release_date',
        'unnecessary_use_of_force'
    ],
    'border_stop': [
        'border_point',
        'stopped_at_border',
        'stopped_previously',
        'target_us_citizenship_status',
        'denial_of_entry',
        'target_nationality',
        'did_authorities_ask_for_device_access',
        'did_authorities_ask_for_social_media_user',
        'did_authorities_ask_for_social_media_pass',
        'did_authorities_ask_about_work',
        'were_devices_searched_or_seized',
    ],
    'denied_access': [
        'politicians_or_public_figures_involved',
    ],
    'equipment_search': [
        'equipment_seized',
        'equipment_broken',
        'status_of_seized_equipment',
        'is_search_warrant_obtained',
        'actor',
    ],
    'physical_attack': [
        'assailant',
        'was_journalist_targeted',
    ],
    'leak': [
        'charged_under_espionage_act',
    ],
    'subpoena': [
        'subpoena_type',
        'subpoena_status',
        'held_in_contempt',
        'detention_status',
        'third_party_in_possession_of_communication',
        'third_party_business',
        'legal_order_type',
    ],
}


class Command(BaseCommand):
    help = 'Creates categories appropriate for development'

    @transaction.atomic
    def handle(self, *args, **options):
        # Remove default wagtail home page, it's not needed.
        Page.objects.filter(slug='home').delete()

        root_page = Page.objects.get(slug='root')
        home_page = HomePageFactory(parent=root_page)
        DevelopmentSiteFactory(root_page=home_page)

        self.stdout.write('Creating categories', ending='')
        for trait, filters in CATEGORIES.items():
            CategoryPageFactory(
                parent=home_page,
                incident_filters=filters,
                **{trait: True}
            )
            self.stdout.write('.', ending='')

        self.stdout.write('')
        for category in CategoryPage.objects.all()[:4]:
            StatBoxFactory(page=home_page, category=category)
