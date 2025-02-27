# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-22 22:26
from __future__ import unicode_literals

import common.blocks
from django.db import migrations
import statistics.blocks
import statistics.registry
import wagtail.blocks
import wagtail.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('incident', '0025_auto_20180222_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidentpage',
            name='body',
            field=wagtail.fields.StreamField((('rich_text', common.blocks.RichTextTemplateBlock(icon='doc-full', label='Rich Text')), ('image', wagtail.images.blocks.ImageChooserBlock()), ('raw_html', wagtail.blocks.RawHTMLBlock()), ('blockquote', wagtail.blocks.StructBlock((('text', wagtail.blocks.RichTextBlock()), ('source_text', wagtail.blocks.RichTextBlock(required=False)), ('source_url', wagtail.blocks.URLBlock(help_text='Source text will link to this url.', required=False))))), ('video', wagtail.blocks.StructBlock((('video', wagtail.embeds.blocks.EmbedBlock()), ('caption', wagtail.blocks.RichTextBlock(help_text='Video description displayed below the video.', required=False)), ('attribution', wagtail.blocks.CharBlock(help_text='Organization / Director.', max_length=255, required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('full-width', 'Full Width')]))))), ('statistics', wagtail.blocks.StructBlock((('visualization', wagtail.blocks.ChoiceBlock(choices=statistics.blocks.get_visualization_choices)), ('dataset', wagtail.blocks.ChoiceBlock(choices=statistics.registry.get_stats_choices)), ('params', wagtail.blocks.CharBlock(help_text='Whitespace-separated list of arguments to be passed to the statistics function', required=False))))))),
        ),
        migrations.AlterField(
            model_name='incidentpageupdates',
            name='body',
            field=wagtail.fields.StreamField((('rich_text', common.blocks.RichTextTemplateBlock(icon='doc-full', label='Rich Text')), ('image', wagtail.images.blocks.ImageChooserBlock()), ('raw_html', wagtail.blocks.RawHTMLBlock()), ('blockquote', wagtail.blocks.StructBlock((('text', wagtail.blocks.RichTextBlock()), ('source_text', wagtail.blocks.RichTextBlock(required=False)), ('source_url', wagtail.blocks.URLBlock(help_text='Source text will link to this url.', required=False))))), ('video', wagtail.blocks.StructBlock((('video', wagtail.embeds.blocks.EmbedBlock()), ('caption', wagtail.blocks.RichTextBlock(help_text='Video description displayed below the video.', required=False)), ('attribution', wagtail.blocks.CharBlock(help_text='Organization / Director.', max_length=255, required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('full-width', 'Full Width')]))))), ('statistics', wagtail.blocks.StructBlock((('visualization', wagtail.blocks.ChoiceBlock(choices=statistics.blocks.get_visualization_choices)), ('dataset', wagtail.blocks.ChoiceBlock(choices=statistics.registry.get_stats_choices)), ('params', wagtail.blocks.CharBlock(help_text='Whitespace-separated list of arguments to be passed to the statistics function', required=False))))))),
        ),
    ]
