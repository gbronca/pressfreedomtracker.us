from wagtail.wagtailcore import blocks
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock

from common.choices import COLOR_CHOICES


class Heading1(blocks.StructBlock):
    content = blocks.CharBlock()

    class Meta:
        template = 'common/blocks/heading_1.html'
        icon = 'title'
        label = 'Heading 1'


class Heading2(blocks.StructBlock):
    content = blocks.CharBlock()

    class Meta:
        template = 'common/blocks/heading_2.html'
        icon = 'title'
        label = 'Heading 2'


class Heading3(blocks.StructBlock):
    content = blocks.CharBlock()

    class Meta:
        template = 'common/blocks/heading_3.html'
        icon = 'title'
        label = 'Heading 3'


ALIGNMENT_CHOICES = (
    ('left', 'Left'),
    ('right', 'Right'),
    ('full-width', 'Full Width'),
)


class AlignedCaptionedImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    caption = blocks.RichTextBlock(required=False)
    alignment = blocks.ChoiceBlock(choices=ALIGNMENT_CHOICES)

    class Meta:
        template = 'common/blocks/aligned_captioned_image.html'
        icon = 'image'
        label = 'Image'


class AlignedCaptionedEmbedBlock(blocks.StructBlock):
    video = EmbedBlock()
    caption = blocks.RichTextBlock(required=False)
    attribution = blocks.CharBlock(max_length=255, required=False)
    alignment = blocks.ChoiceBlock(choices=ALIGNMENT_CHOICES)

    class Meta:
        template = 'common/blocks/aligned_captioned_embed.html'
        icon = 'media'
        label = 'Video'


class StyledTextBlock(blocks.StructBlock):
    TEXT_ALIGN_CHOICES = (
        ('left', 'Left'),
        ('center', 'Center'),
        ('right', 'Right'),
    )

    FONT_SIZE_CHOICES = (
        ('small', 'Small'),
        ('normal', 'Normal'),
        ('large', 'Large'),
        ('jumbo', 'Jumbo'),
    )

    FONT_FAMILY_CHOICES = (
        ('sans-serif', 'Sans Serif'),
        ('serif', 'Serif'),
    )

    text = blocks.RichTextBlock()
    background_color = blocks.ChoiceBlock(choices=COLOR_CHOICES, default='white')
    text_align = blocks.ChoiceBlock(choices=TEXT_ALIGN_CHOICES, default='left')
    font_size = blocks.ChoiceBlock(choices=FONT_SIZE_CHOICES, default='normal')
    font_family = blocks.ChoiceBlock(choices=FONT_FAMILY_CHOICES, default='sans-serif')

    class Meta:
        template = 'common/blocks/styled_text.html'
        icon = 'doc-full'
        label = 'Styled Text Block'