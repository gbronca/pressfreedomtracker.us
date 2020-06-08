# Generated by Django 2.2.12 on 2020-06-08 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('incident', '0051_topicpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='topicpage',
            name='incident_index_page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='incident.IncidentIndexPage'),
        ),
        migrations.AddField(
            model_name='topicpage',
            name='layout',
            field=models.CharField(choices=[('by_incident', 'By Incident'), ('by_category', 'By Category')], default='by_incident', max_length=255),
        ),
    ]
