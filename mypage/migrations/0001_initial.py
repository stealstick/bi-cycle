# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20161029_0210'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cloth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('text', models.TextField(null=True)),
                ('update_date', models.DateTimeField()),
                ('cloth', models.ForeignKey(null=True, related_name='clother_name', to='main.Cloth')),
                ('lenter', models.ForeignKey(null=True, related_name='lenter_lother', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(null=True, related_name='owner_lother', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
