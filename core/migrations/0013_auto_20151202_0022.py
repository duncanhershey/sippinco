# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='wifi',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None Available'), (1, b'Patchy'), (2, b'Strong')]),
        ),
    ]
