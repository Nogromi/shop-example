# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-09 14:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20170509_1747'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='product',
        ),
    ]
