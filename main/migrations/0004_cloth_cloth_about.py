# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20161027_0821'),
    ]

    operations = [
        migrations.AddField(
            model_name='cloth',
            name='cloth_about',
            field=models.TextField(null=True),
        ),
    ]
