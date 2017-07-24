# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cloth',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('cloth_name', models.CharField(max_length=40)),
                ('size', models.CharField(max_length=20)),
                ('bo_prize', models.IntegerField(default=1)),
                ('lent_prize', models.IntegerField(default=1)),
                ('cloth_img', models.CharField(max_length=20)),
                ('cloth_intro', models.TextField()),
            ],
        ),
    ]
