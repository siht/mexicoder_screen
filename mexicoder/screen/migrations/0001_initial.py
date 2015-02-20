# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('common_name', models.CharField(max_length=20)),
                ('nation', models.CharField(max_length=20)),
                ('height', models.FloatField()),
                ('foot', models.CharField(max_length=5, choices=[(b'Left', b'Left'), (b'Right', b'Right')])),
                ('club', models.ForeignKey(to='screen.Club')),
                ('leage', models.ForeignKey(to='screen.League')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeamCoach',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('common_name', models.CharField(max_length=20)),
                ('nation', models.CharField(max_length=20)),
                ('club', models.ForeignKey(to='screen.Club')),
                ('leage', models.ForeignKey(to='screen.League')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
