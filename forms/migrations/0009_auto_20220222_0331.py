# Generated by Django 3.2.11 on 2022-02-22 03:31

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0008_formfield_clean_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, help_text='Optional: description for the field group', max_length=255, null=True)),
                ('template', models.CharField(choices=[('text', 'Text fields'), ('date_single', 'Single date'), ('choices', 'Choices')], default='text', help_text='Select template used to display this field group', max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupedFormField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('clean_name', models.CharField(blank=True, default='', help_text='Safe name of the form field, the label converted to ascii_snake_case', max_length=255, verbose_name='name')),
                ('label', models.CharField(help_text='The label of the form field', max_length=255, verbose_name='label')),
                ('field_type', models.CharField(choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('multiselect', 'Multiple select'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time'), ('hidden', 'Hidden field')], max_length=16, verbose_name='field type')),
                ('required', models.BooleanField(default=True, verbose_name='required')),
                ('choices', models.TextField(blank=True, help_text='Comma separated list of choices. Only applicable in checkboxes, radio and dropdown.', verbose_name='choices')),
                ('default_value', models.CharField(blank=True, help_text='Default value. Comma separated values supported for checkboxes.', max_length=255, verbose_name='default value')),
                ('help_text', models.CharField(blank=True, max_length=255, verbose_name='help text')),
                ('placeholder', models.CharField(blank=True, help_text='Optional: placeholder for the field', max_length=255, null=True)),
                ('append_to_subject', models.BooleanField(default=False, help_text='Add the contents of this field to the subject of the email sent by this from.  All fields with this checked will be appended.')),
                ('use_as_reply_to', models.BooleanField(default=False, help_text='Use the contents of this field as the Reply-To header of the email sent by this from.  Only one field per form can have this checked.')),
                ('group', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_fields', to='forms.fieldgroup')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='formpage',
            name='form_intro',
            field=models.TextField(blank=True, help_text='Optional: short intro for the form', null=True),
        ),
        migrations.AddField(
            model_name='formpage',
            name='outro_text',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Optional: text for the page outro', null=True),
        ),
        migrations.AddField(
            model_name='formpage',
            name='outro_title',
            field=models.CharField(blank=True, help_text='Optional: title for the page outro', max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='FormField',
        ),
        migrations.AddField(
            model_name='fieldgroup',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='field_groups', to='forms.formpage'),
        ),
        migrations.AddConstraint(
            model_name='groupedformfield',
            constraint=models.UniqueConstraint(condition=models.Q(('use_as_reply_to', True)), fields=('group',), name='only_one_reply_to_form_field'),
        ),
    ]