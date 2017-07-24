# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20161029_0210'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mypage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Send',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('text', models.TextField(null=True)),
                ('update_date', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='cloth',
            name='cloth',
        ),
        migrations.RemoveField(
            model_name='cloth',
            name='lenter',
        ),
        migrations.RemoveField(
            model_name='cloth',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Cloth',
        ),
        migrations.AddField(
            model_name='send',
            name='cloth',
            field=models.ForeignKey(related_name='clother_name', to='main.Cloth', null=True),
        ),
        migrations.AddField(
            model_name='send',
            name='owner',
            field=models.ForeignKey(related_name='owner_lother', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='send',
            name='resiver',
            field=models.ForeignKey(related_name='lenter_lother', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
