# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-15 21:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incident', '0021_auto_20180208_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidentpage',
            name='actor',
            field=models.CharField(blank=True, choices=[('UNKNOWN', 'unknown'), ('LAW_ENFORCEMENT', 'law enforcement'), ('PRIVATE_SECURITY', 'private security'), ('POLITICIAN', 'politician'), ('PUBLIC_FIGURE', 'public figure'), ('PRIVATE_INDIVIDUAL', 'private individual')], max_length=255, null=True, verbose_name='Actor'),
        ),
        migrations.AlterField(
            model_name='incidentpage',
            name='arrest_status',
            field=models.CharField(blank=True, choices=[('UNKNOWN', 'unknown'), ('DETAINED_NO_PROCESSING', 'detained and released without being processed'), ('DETAINED_CUSTODY', 'detained and still in custody'), ('ARRESTED_CUSTODY', 'arrested and still in custody'), ('ARRESTED_RELEASED', 'arrested and released')], max_length=255, null=True, verbose_name='Arrest status'),
        ),
        migrations.AlterField(
            model_name='incidentpage',
            name='assailant',
            field=models.CharField(blank=True, choices=[('UNKNOWN', 'unknown'), ('LAW_ENFORCEMENT', 'law enforcement'), ('PRIVATE_SECURITY', 'private security'), ('POLITICIAN', 'politician'), ('PUBLIC_FIGURE', 'public figure'), ('PRIVATE_INDIVIDUAL', 'private individual')], max_length=255, null=True, verbose_name='Assailant'),
        ),
        migrations.AlterField(
            model_name='incidentpage',
            name='border_point',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Border point'),
        ),
        migrations.AlterField(
            model_name='incidentpage',
            name='charged_under_espionage_act',
            field=models.BooleanField(default=False, verbose_name='Charged under espionage act?'),
        ),
        migrations.AlterField(
            model_name='incidentpage',
            name='detention_date',
            field=models.DateField(blank=True, help_text='This field will default to the date field if not specified.', null=True, verbose_name='Detention date'),
        ),
        migrations.AlterField(
            model_name='incidentpage',
            name='detention_status',
            field=models.CharField(blank=True, choices=[('HELD_IN_CONTEMPT_NO_JAIL', 'held in contempt but not jailed'), ('IN_JAIL', 'in jail'), ('RELEASED', 'released from jail')], max_length=255, null=True, verbose_name='Detention status'),
        ),
        migrations.AlterField(
            model_name='incidentpage',
            name='did_authorities_ask_for_device_access',
            field=models.CharField(blank=True, choices=[('NOTHING', 'unknown'), ('JUST_TRUE', 'yes'), ('JUST_FALSE', 'no')], max_length=255, null=True, verbose_name='Did authorities ask for device access?'),
        ),
        migrations.AlterField(
            model_name='incidentpage',
            name='did_authorities_ask_for_social_media_pass',
            field=models.CharField(blank=True, choices=[('NOTHING', 'unknown'), ('JUST_TRUE', 'yes'), ('JUST_FALSE', 'no')], max_length=255, null=True, verbose_name='Did authorities ask for social media password?'),
        ),
        migrations.AlterField(
            model_name='incidentpage',
            name='did_authorities_ask_for_social_media_user',
            field=models.CharField(blank=True, choices=[('NOTHING', 'unknown'), ('JUST_TRUE', 'yes'), ('JUST_FALSE', 'no')], max_length=255, null=True, verbose_name='Did authorities ask for social media username?'),
        ),
        migrations.AlterField(
            model_name='incidentpage',
            name='is_search_warrant_obtained',
            field=models.BooleanField(default=False, verbose_name='Search warrant obtained?'),
        ),
        migrations.AlterField(
            model_name='incidentpage',
            name='lawsuit_name',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Lawsuit name'),
        ),
        migrations.AlterField(
            model_name='incidentpage',
            name='legal_order_type',
            field=models.CharField(blank=True, choices=[('SUBPOENA', 'subpoena'), ('2703', '2703(d) court order'), ('WARRANT', 'warrant'), ('NATIONAL_SECURITY_LETTER', 'national security letter'), ('FISA', 'FISA order'), ('OTHER', 'other')], max_length=255, null=True, verbose_name='Legal order type'),
        ),
        migrations.AlterField(
            model_name='incidentpage',
            name='release_date',
            field=models.DateField(blank=True, null=True, verbose_name='Release date'),
        ),
        migrations.AlterField(
            model_name='incidentpage',
            name='status_of_charges',
            field=models.CharField(blank=True, choices=[('UNKNOWN', 'unknown'), ('NOT_CHARGED', 'not charged'), ('CHARGES_PENDING', 'charges pending'), ('CHARGES_DROPPED', 'charges dropped'), ('CONVICTED', 'convicted'), ('ACQUITTED', 'acquitted'), ('PENDING_APPEAL', 'pending appeal')], max_length=255, null=True, verbose_name='Status of charges'),
        ),
        migrations.AlterField(
            model_name='incidentpage',
            name='status_of_prior_restraint',
            field=models.CharField(blank=True, choices=[('PENDING', 'pending'), ('DROPPED', 'dropped'), ('STRUCK_DOWN', 'struck down'), ('UPHELD', 'upheld')], max_length=255, null=True, verbose_name='Status of prior restraint'),
        ),
        migrations.AlterField(
            model_name='incidentpage',
            name='status_of_seized_equipment',
            field=models.CharField(blank=True, choices=[('UNKNOWN', 'unknown'), ('CUSTODY', 'in custody'), ('RETURNED_FULL', 'returned in full'), ('RETURNED_PART', 'returned in part')], max_length=255, null=True, verbose_name='Status of seized equipment'),
        ),
        migrations.AlterField(
            model_name='incidentpage',
            name='stopped_at_border',
            field=models.BooleanField(default=False, verbose_name='Stopped at border?'),
        ),
        migrations.AlterField(
            model_name='incidentpage',
            name='subpoena_status',
            field=models.CharField(blank=True, choices=[('PENDING', 'pending'), ('DROPPED', 'dropped'), ('QUASHED', 'quashed'), ('UPHELD', 'upheld'), ('CARRIED_OUT', 'carried out')], max_length=255, null=True, verbose_name='Subpoena status'),
        ),
        migrations.AlterField(
            model_name='incidentpage',
            name='subpoena_type',
            field=models.CharField(blank=True, choices=[('TESTIMONY_ABOUT_SOURCE', 'testimony about confidential source'), ('OTHER_TESTIMONY', 'other testimony'), ('JOURNALIST_COMMUNICATIONS', 'journalist communications or work product')], max_length=255, null=True, verbose_name='Subpoena type'),
        ),
        migrations.AlterField(
            model_name='incidentpage',
            name='target_us_citizenship_status',
            field=models.CharField(blank=True, choices=[('US_CITIZEN', 'U.S. citizen'), ('PERMANENT_RESIDENT', 'U.S. permanent resident (green card)'), ('NON_RESIDENT', 'U.S. non-resident')], max_length=255, null=True, verbose_name='US Citizenship Status'),
        ),
        migrations.AlterField(
            model_name='incidentpage',
            name='third_party_business',
            field=models.CharField(blank=True, choices=[('TELECOM', 'telecom company'), ('TECH_COMPANY', 'tech company'), ('ISP', 'internet service provider'), ('FINANCIAL', 'bank/financial institution'), ('TRAVEL', 'travel company'), ('OTHER', 'other')], max_length=255, null=True, verbose_name='Third party business'),
        ),
        migrations.AlterField(
            model_name='incidentpage',
            name='third_party_in_possession_of_communications',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='Third party in possession of communications'),
        ),
        migrations.AlterField(
            model_name='incidentpage',
            name='unnecessary_use_of_force',
            field=models.BooleanField(default=False, verbose_name='Unnecessary use of force?'),
        ),
        migrations.AlterField(
            model_name='incidentpage',
            name='was_journalist_targeted',
            field=models.CharField(blank=True, choices=[('NOTHING', 'unknown'), ('JUST_TRUE', 'yes'), ('JUST_FALSE', 'no')], max_length=255, null=True, verbose_name='Was journalist targeted?'),
        ),
        migrations.AlterField(
            model_name='incidentpage',
            name='were_devices_searched_or_seized',
            field=models.CharField(blank=True, choices=[('NOTHING', 'unknown'), ('JUST_TRUE', 'yes'), ('JUST_FALSE', 'no')], max_length=255, null=True, verbose_name='Were devices searched or seized?'),
        ),
    ]