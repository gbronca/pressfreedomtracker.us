# Generated by Django 3.2.11 on 2022-02-16 08:05

import common.blocks
from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0082_auto_20220120_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simplepage',
            name='body',
            field=wagtail.core.fields.StreamField([('text', wagtail.core.blocks.StructBlock([('text', common.blocks.RichTextTemplateBlock(features=['bold', 'italic', 'h2', 'h3', 'h4', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image', 'code', 'numincidents'])), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('white', 'White'), ('eastern-blue', 'Eastern Blue'), ('gamboge', 'Gamboge'), ('green', 'Green'), ('pink', 'Pink'), ('red', 'Red'), ('royal-blue', 'Royal Blue'), ('teal', 'Teal'), ('violet', 'Violet'), ('dark-gray', 'Dark Gray')])), ('text_align', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('font_size', wagtail.core.blocks.ChoiceBlock(choices=[('small', 'Small'), ('normal', 'Normal'), ('large', 'Large'), ('jumbo', 'Jumbo')])), ('font_family', wagtail.core.blocks.ChoiceBlock(choices=[('sans-serif', 'Sans Serif'), ('serif', 'Serif')]))], label='Text', template='common/blocks/styled_text_full_bleed.html')), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.RichTextBlock(help_text='Image description displayed below the image. Organization/Photographer can be set via the image attribution.', required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('full-width', 'Full Width')]))])), ('raw_html', wagtail.core.blocks.RawHTMLBlock()), ('tweet', wagtail.core.blocks.StructBlock([('tweet', wagtail.embeds.blocks.EmbedBlock())])), ('blockquote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock()), ('source_text', wagtail.core.blocks.RichTextBlock(required=False)), ('source_url', wagtail.core.blocks.URLBlock(help_text='Source text will link to this url.', required=False))])), ('list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(label='List Item'), template='common/blocks/list_block_columns.html')), ('logo_list', common.blocks.LogoListBlock()), ('video', wagtail.core.blocks.StructBlock([('video', wagtail.embeds.blocks.EmbedBlock()), ('caption', wagtail.core.blocks.RichTextBlock(help_text='Video description displayed below the video.', required=False)), ('attribution', wagtail.core.blocks.CharBlock(help_text='Organization / Director.', max_length=255, required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('full-width', 'Full Width')]))])), ('heading_1', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.CharBlock())])), ('heading_2', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.CharBlock())])), ('heading_3', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.CharBlock())])), ('email_signup', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Defaults to sitewide setting', label='Call to action text', required=False)), ('success_text', wagtail.core.blocks.CharBlock(help_text='To be displayed after a successful signup. Defaults to sitewide setting', label='Success text', required=False))])), ('info_table', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(help_text='Heading of the info table')), ('table', wagtail.core.blocks.StreamBlock([('page_links', wagtail.core.blocks.StructBlock([('cta_label', wagtail.core.blocks.CharBlock(help_text='Label to be displayed for row link, e.g. "Read the bio", "Contact us", "Visit the page", etc.')), ('table_data', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('page', wagtail.core.blocks.PageChooserBlock()), ('title', wagtail.core.blocks.CharBlock(help_text='Optional: defaults to page title', required=False)), ('description', wagtail.core.blocks.CharBlock())], icon='list-ul', label='Table row')))])), ('email_addresses', wagtail.core.blocks.StructBlock([('cta_label', wagtail.core.blocks.CharBlock(help_text='Label to be displayed for row link, e.g. "Read the bio", "Contact us", "Visit the page", etc.')), ('table_data', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('email', wagtail.core.blocks.EmailBlock())], icon='list-ul', label='Table row')))])), ('external_links', wagtail.core.blocks.StructBlock([('cta_label', wagtail.core.blocks.CharBlock(help_text='Label to be displayed for row link, e.g. "Read the bio", "Contact us", "Visit the page", etc.')), ('table_data', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.core.blocks.CharBlock()), ('url', wagtail.core.blocks.URLBlock())], icon='list-ul', label='Table row')))])), ('plain_text', wagtail.core.blocks.StructBlock([('table_data', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.CharBlock())], icon='list-ul', label='Table row')))]))], icon='list-ul', label='Table type', max_num=1))]))]),
        ),
    ]
