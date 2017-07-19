# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 23:47
from __future__ import unicode_literals

import common.blocks
from django.db import migrations
import statistics.blocks
import statistics.registry
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rich_text_blockquote_blocks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('text', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('background_color', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('eastern-blue', 'Eastern Blue'), ('gamboge', 'Gamboge'), ('green', 'Green'), ('pink', 'Pink'), ('red', 'Red'), ('royal-blue', 'Royal Blue'), ('teal', 'Teal'), ('violet', 'Violet'), ('white', 'White')])), ('text_align', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('font_size', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('small', 'Small'), ('normal', 'Normal'), ('large', 'Large'), ('jumbo', 'Jumbo')])), ('font_family', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('sans-serif', 'Sans Serif'), ('serif', 'Serif')]))), label='Text', template='common/blocks/styled_text_full_bleed.html')), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('caption', wagtail.wagtailcore.blocks.RichTextBlock(help_text='Image description displayed below the image. Organization/Photographer can be set via the image attribution.', required=False)), ('alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('full-width', 'Full Width')]))))), ('raw_html', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('blockquote', common.blocks.RichTextBlockQuoteBlock()), ('list', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock(label='List Item'), template='common/blocks/list_block_columns.html')), ('video', wagtail.wagtailcore.blocks.StructBlock((('video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('caption', wagtail.wagtailcore.blocks.RichTextBlock(help_text='Video description displayed below the video.', required=False)), ('attribution', wagtail.wagtailcore.blocks.CharBlock(help_text='Organization / Director.', max_length=255, required=False)), ('alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('full-width', 'Full Width')]))))), ('heading_1', wagtail.wagtailcore.blocks.StructBlock((('content', wagtail.wagtailcore.blocks.CharBlock()),))), ('heading_2', wagtail.wagtailcore.blocks.StructBlock((('content', wagtail.wagtailcore.blocks.CharBlock()),))), ('heading_3', wagtail.wagtailcore.blocks.StructBlock((('content', wagtail.wagtailcore.blocks.CharBlock()),))), ('statistics', wagtail.wagtailcore.blocks.StructBlock((('visualization', wagtail.wagtailcore.blocks.ChoiceBlock(choices=statistics.blocks.get_visualization_choices)), ('dataset', wagtail.wagtailcore.blocks.ChoiceBlock(choices=statistics.registry.get_stats_choices)), ('params', wagtail.wagtailcore.blocks.CharBlock(help_text='Whitespace-separated list of arguments to be passed to the statistics function', required=False))))))),
        ),
    ]