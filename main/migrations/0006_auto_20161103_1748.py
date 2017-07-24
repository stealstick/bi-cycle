# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20161029_0210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloth',
            name='bo_prize',
            field=models.CharField(null=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='cloth',
            name='lent_prize',
            field=models.CharField(null=True, max_length=20),
        ),
    ]
