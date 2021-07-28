# Generated by Django 2.2.24 on 2021-06-23 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20200203_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogindexpage',
            name='feed_per_page',
            field=models.PositiveIntegerField(default=20, help_text='Maximum number of posts to be included per page in the syndication feed.'),
        ),
    ]