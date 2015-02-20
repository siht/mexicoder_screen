# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='attack',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='club',
            name='defense',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='club',
            name='midfield',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='club',
            name='rating',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
