# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-28 17:08
from __future__ import unicode_literals

from django.db import migrations, models
import modelcluster.fields


def convert_tags_to_many_to_many(page_model, item_model, relation_name):
    for page in page_model.objects.all():
        # The fake model given in migrations doesn't include the typical
        # related manager functionality we need, so you get this awful
        # snippet.
        tmp_relations = getattr(page, '_tmp_' + relation_name).through.objects.filter(content_object=page)
        for relation in tmp_relations:
            item, _ = item_model.objects.get_or_create(title=relation.tag.name)
            getattr(page, relation_name).add(item)
        getattr(page, relation_name).commit()


def migrate_tags(apps, schema_editor):
    IncidentPage = apps.get_model('incident', 'IncidentPage')
    CommonTag = apps.get_model('common', 'CommonTag')
    convert_tags_to_many_to_many(IncidentPage, CommonTag, 'tags')


def migrate_targets(apps, schema_editor):
    IncidentPage = apps.get_model('incident', 'IncidentPage')
    Target = apps.get_model('incident', 'Target')
    convert_tags_to_many_to_many(IncidentPage, Target, 'targets')
    convert_tags_to_many_to_many(IncidentPage, Target, 'targets_whose_communications_were_obtained')


def migrate_charges(apps, schema_editor):
    IncidentPage = apps.get_model('incident', 'IncidentPage')
    Charge = apps.get_model('incident', 'Charge')
    convert_tags_to_many_to_many(IncidentPage, Charge, 'current_charges')
    convert_tags_to_many_to_many(IncidentPage, Charge, 'dropped_charges')


def migrate_nationalities(apps, schema_editor):
    IncidentPage = apps.get_model('incident', 'IncidentPage')
    Nationality = apps.get_model('incident', 'Nationality')
    convert_tags_to_many_to_many(IncidentPage, Nationality, 'target_nationality')


def migrate_politicians_or_public(apps, schema_editor):
    IncidentPage = apps.get_model('incident', 'IncidentPage')
    PoliticianOrPublic = apps.get_model('incident', 'PoliticianOrPublic')
    convert_tags_to_many_to_many(IncidentPage, PoliticianOrPublic, 'politicians_or_public_figures_involved')


class Migration(migrations.Migration):

    dependencies = [
        ('incident', '0005_merge_20170626_2248'),
        ('common', '0006_add_common_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incidentpage',
            old_name='tags',
            new_name='_tmp_tags',
        ),
        migrations.AddField(
            model_name='incidentpage',
            name='tags',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, related_name='tagged_items', to='common.CommonTag', verbose_name='Tags'),
        ),
        migrations.RunPython(migrate_tags),
        migrations.RemoveField(
            model_name='incidentpage',
            name='_tmp_tags'
        ),

        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='incidentpage',
            old_name='targets',
            new_name='_tmp_targets',
        ),
        migrations.AddField(
            model_name='incidentpage',
            name='targets',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, related_name='targets_incidents', to='incident.Target', verbose_name='Targets (Journalists/Organizations)'),
        ),
        migrations.RenameField(
            model_name='incidentpage',
            old_name='targets_whose_communications_were_obtained',
            new_name='_tmp_targets_whose_communications_were_obtained',
        ),
        migrations.AddField(
            model_name='incidentpage',
            name='targets_whose_communications_were_obtained',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, related_name='targets_communications_obtained_incidents', to='incident.Target', verbose_name='Journalists/Organizations whose communications were obtained in leak investigation'),
        ),
        migrations.RunPython(migrate_targets),
        migrations.RemoveField(
            model_name='incidentpage',
            name='_tmp_targets'
        ),
        migrations.RemoveField(
            model_name='incidentpage',
            name='_tmp_targets_whose_communications_were_obtained'
        ),
        migrations.DeleteModel(name='TargetsTag'),
        migrations.DeleteModel(name='TargetsCommunicationsObtainedTag'),

        migrations.CreateModel(
            name='Charge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='incidentpage',
            old_name='current_charges',
            new_name='_tmp_current_charges',
        ),
        migrations.RenameField(
            model_name='incidentpage',
            old_name='dropped_charges',
            new_name='_tmp_dropped_charges',
        ),
        migrations.AddField(
            model_name='incidentpage',
            name='current_charges',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, related_name='current_charge_incidents', to='incident.Charge', verbose_name='Current Charges'),
        ),
        migrations.AddField(
            model_name='incidentpage',
            name='dropped_charges',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, related_name='dropped_charge_incidents', to='incident.Charge', verbose_name='Dropped Charges'),
        ),
        migrations.RunPython(migrate_charges),
        migrations.RemoveField(
            model_name='incidentpage',
            name='_tmp_current_charges'
        ),
        migrations.RemoveField(
            model_name='incidentpage',
            name='_tmp_dropped_charges'
        ),
        migrations.DeleteModel(name='CurrentChargesTag'),
        migrations.DeleteModel(name='DroppedChargesTag'),

        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='incidentpage',
            old_name='target_nationality',
            new_name='_tmp_target_nationality',
        ),
        migrations.AddField(
            model_name='incidentpage',
            name='target_nationality',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, related_name='nationality_incidents', to='incident.Nationality', verbose_name='Target Nationality'),
        ),
        migrations.RunPython(migrate_nationalities),
        migrations.RemoveField(
            model_name='incidentpage',
            name='_tmp_target_nationality'
        ),
        migrations.DeleteModel(name='NationalityTag'),

        migrations.CreateModel(
            name='PoliticianOrPublic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='incidentpage',
            old_name='politicians_or_public_figures_involved',
            new_name='_tmp_politicians_or_public_figures_involved',
        ),
        migrations.AddField(
            model_name='incidentpage',
            name='politicians_or_public_figures_involved',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, related_name='politicians_or_public_incidents', to='incident.PoliticianOrPublic', verbose_name='Politicians or public officials involved'),
        ),
        migrations.RunPython(migrate_politicians_or_public),
        migrations.RemoveField(
            model_name='incidentpage',
            name='_tmp_politicians_or_public_figures_involved'
        ),
        migrations.DeleteModel(name='PoliticiansOrPublicTag'),
    ]
