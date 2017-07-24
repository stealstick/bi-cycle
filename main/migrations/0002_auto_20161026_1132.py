# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cloth',
            name='lenter',
            field=models.ForeignKey(null=True, related_name='lenter_clother', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cloth',
            name='owner',
            field=models.ForeignKey(null=True, related_name='owner_clother', to=settings.AUTH_USER_MODEL),
        ),
    ]
