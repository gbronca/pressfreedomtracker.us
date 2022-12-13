# Generated by Django 2.2.9 on 2020-02-03 19:15

import common.blocks
from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0062_auto_20191023_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simplepage',
            name='body',
            field=wagtail.fields.StreamField([('text', wagtail.blocks.StructBlock([('text', common.blocks.RichTextTemplateBlock(features=['bold', 'italic', 'h2', 'h3', 'h4', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image', 'code'])), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('white', 'White'), ('eastern-blue', 'Eastern Blue'), ('gamboge', 'Gamboge'), ('green', 'Green'), ('pink', 'Pink'), ('red', 'Red'), ('royal-blue', 'Royal Blue'), ('teal', 'Teal'), ('violet', 'Violet'), ('dark-gray', 'Dark Gray')])), ('text_align', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('font_size', wagtail.blocks.ChoiceBlock(choices=[('small', 'Small'), ('normal', 'Normal'), ('large', 'Large'), ('jumbo', 'Jumbo')])), ('font_family', wagtail.blocks.ChoiceBlock(choices=[('sans-serif', 'Sans Serif'), ('serif', 'Serif')]))], label='Text', template='common/blocks/styled_text_full_bleed.html')), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.blocks.RichTextBlock(help_text='Image description displayed below the image. Organization/Photographer can be set via the image attribution.', required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('full-width', 'Full Width')]))])), ('raw_html', wagtail.blocks.RawHTMLBlock()), ('tweet', wagtail.blocks.StructBlock([('tweet', wagtail.embeds.blocks.EmbedBlock())])), ('blockquote', wagtail.blocks.StructBlock([('text', wagtail.blocks.RichTextBlock()), ('source_text', wagtail.blocks.RichTextBlock(required=False)), ('source_url', wagtail.blocks.URLBlock(help_text='Source text will link to this url.', required=False))])), ('list', wagtail.blocks.ListBlock(wagtail.blocks.CharBlock(label='List Item'), template='common/blocks/list_block_columns.html')), ('logo_list', common.blocks.LogoListBlock()), ('video', wagtail.blocks.StructBlock([('video', wagtail.embeds.blocks.EmbedBlock()), ('caption', wagtail.blocks.RichTextBlock(help_text='Video description displayed below the video.', required=False)), ('attribution', wagtail.blocks.CharBlock(help_text='Organization / Director.', max_length=255, required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('full-width', 'Full Width')]))])), ('heading_1', wagtail.blocks.StructBlock([('content', wagtail.blocks.CharBlock())])), ('heading_2', wagtail.blocks.StructBlock([('content', wagtail.blocks.CharBlock())])), ('heading_3', wagtail.blocks.StructBlock([('content', wagtail.blocks.CharBlock())])), ('email_signup', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(help_text='Defaults to sitewide setting', label='Call to action text', required=False)), ('success_text', wagtail.blocks.CharBlock(help_text='To be displayed after a successful signup. Defaults to sitewide setting', label='Success text', required=False))]))]),
        ),
        migrations.AlterField(
            model_name='simplepagewithsidebar',
            name='body',
            field=wagtail.fields.StreamField([('text', wagtail.blocks.StructBlock([('text', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'h2', 'h3', 'h4', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image', 'code'])), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('white', 'White'), ('eastern-blue', 'Eastern Blue'), ('gamboge', 'Gamboge'), ('green', 'Green'), ('pink', 'Pink'), ('red', 'Red'), ('royal-blue', 'Royal Blue'), ('teal', 'Teal'), ('violet', 'Violet'), ('dark-gray', 'Dark Gray')])), ('text_align', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('font_size', wagtail.blocks.ChoiceBlock(choices=[('small', 'Small'), ('normal', 'Normal'), ('large', 'Large'), ('jumbo', 'Jumbo')])), ('font_family', wagtail.blocks.ChoiceBlock(choices=[('sans-serif', 'Sans Serif'), ('serif', 'Serif')]))], label='Text')), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.blocks.RichTextBlock(help_text='Image description displayed below the image. Organization/Photographer can be set via the image attribution.', required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('full-width', 'Full Width')]))])), ('raw_html', wagtail.blocks.RawHTMLBlock()), ('tweet', wagtail.blocks.StructBlock([('tweet', wagtail.embeds.blocks.EmbedBlock())])), ('blockquote', wagtail.blocks.StructBlock([('text', wagtail.blocks.RichTextBlock()), ('source_text', wagtail.blocks.RichTextBlock(required=False)), ('source_url', wagtail.blocks.URLBlock(help_text='Source text will link to this url.', required=False))])), ('list', wagtail.blocks.ListBlock(wagtail.blocks.CharBlock(label='List Item'), template='common/blocks/list_block_columns.html')), ('logo_list', common.blocks.LogoListBlock()), ('video', wagtail.blocks.StructBlock([('video', wagtail.embeds.blocks.EmbedBlock()), ('caption', wagtail.blocks.RichTextBlock(help_text='Video description displayed below the video.', required=False)), ('attribution', wagtail.blocks.CharBlock(help_text='Organization / Director.', max_length=255, required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('full-width', 'Full Width')]))])), ('heading_1', wagtail.blocks.StructBlock([('content', wagtail.blocks.CharBlock())])), ('heading_2', wagtail.blocks.StructBlock([('content', wagtail.blocks.CharBlock())])), ('heading_3', wagtail.blocks.StructBlock([('content', wagtail.blocks.CharBlock())])), ('email_signup', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(help_text='Defaults to sitewide setting', label='Call to action text', required=False)), ('success_text', wagtail.blocks.CharBlock(help_text='To be displayed after a successful signup. Defaults to sitewide setting', label='Success text', required=False))]))]),
        ),
    ]
