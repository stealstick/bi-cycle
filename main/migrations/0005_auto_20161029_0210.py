# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_cloth_cloth_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloth',
            name='cloth_img',
            field=models.ImageField(default='cloth_image/default.png', upload_to='cloth_image'),
        ),
    ]
