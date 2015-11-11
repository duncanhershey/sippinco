# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='area',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'Botley'), (1, b'Central'), (2, b'Cowley'), (3, b'Headington'), (4, b'Jericho'), (5, b'Summertown')]),
        ),
        migrations.AddField(
            model_name='location',
            name='foodserved',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AddField(
            model_name='location',
            name='outdoor',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AddField(
            model_name='location',
            name='seating',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Minimal'), (2, b'Some'), (3, b'Ample')]),
        ),
        migrations.AddField(
            model_name='location',
            name='wifi',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None Available'), (1, b'Unstable/Sometimes Ok'), (3, b'Strong')]),
        ),
    ]
