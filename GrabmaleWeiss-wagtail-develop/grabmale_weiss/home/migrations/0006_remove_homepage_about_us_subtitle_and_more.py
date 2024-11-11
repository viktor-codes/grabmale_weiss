# Generated by Django 5.1.2 on 2024-11-09 15:46

import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_homepage_about_us_images_homepage_about_us_subtitle_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='about_us_subtitle',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='additional_services_subtitle',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='additional_services_text',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='additional_services_title',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='services_footer_note',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='timeline_date',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='timeline_description',
        ),
        migrations.AddField(
            model_name='homepage',
            name='about_us_stories',
            field=wagtail.fields.StreamField([('story', 3)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'required': True, 'verbose_name': 'Subtitle'}), 1: ('wagtail.blocks.CharBlock', (), {'required': True, 'verbose_name': 'Timeline Date'}), 2: ('wagtail.blocks.RichTextBlock', (), {'required': True, 'verbose_name': 'Story Text'}), 3: ('wagtail.blocks.StructBlock', [[('subtitle', 0), ('timeline_date', 1), ('story_text', 2)]], {'verbose_name': 'Story'})}, verbose_name='About Us Stories'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='features_footer_note',
            field=models.CharField(default='', max_length=255, verbose_name='Features Note'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='features_items',
            field=wagtail.fields.StreamField([('features_item', 2)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'required': True, 'verbose_name': 'Features Subtitle'}), 1: ('wagtail.blocks.RichTextBlock', (), {'required': True, 'verbose_name': 'Features Text'}), 2: ('wagtail.blocks.StructBlock', [[('subtitle', 0), ('features_text', 1)]], {'verbose_name': 'Features Item'})}, verbose_name='Features Items'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='features_title',
            field=models.CharField(default='', max_length=255, verbose_name='Features Title'),
        ),
    ]
