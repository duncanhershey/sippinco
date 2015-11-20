# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20151111_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='fb_page',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='location',
            name='fb_page_label',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
    ]
