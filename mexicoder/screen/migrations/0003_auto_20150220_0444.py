# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0002_auto_20150220_0334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='leage',
            new_name='league',
        ),
        migrations.RenameField(
            model_name='teamcoach',
            old_name='leage',
            new_name='league',
        ),
    ]
