# Generated by Django 3.2.12 on 2022-03-14 07:02

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0084_auto_20220311_0740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorypage',
            name='methodology',
            field=wagtail.fields.RichTextField(blank=True, help_text='Detailed description of how we track the data for this particular category.', null=True),
        ),
    ]
