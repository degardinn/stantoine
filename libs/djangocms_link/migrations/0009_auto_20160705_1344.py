# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 17:44
from __future__ import unicode_literals

from django.db import migrations
import djangocms_attributes_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_link', '0008_link_attributes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='attributes',
            field=djangocms_attributes_field.fields.AttributesField(blank=True, default=dict, help_text='Optional. Link HTML tag attributes', verbose_name='link tag attributes'),
        ),
    ]
