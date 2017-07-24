# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20161026_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='cloth',
            name='category',
            field=models.CharField(null=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='cloth',
            name='cloth_img',
            field=models.CharField(max_length=40),
        ),
    ]
