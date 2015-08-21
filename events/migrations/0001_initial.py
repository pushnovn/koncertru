# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('start_time', models.DateTimeField()),
                ('finish_time', models.DateTimeField(blank=True)),
                ('image', models.ImageField(upload_to='static/events_images')),
                ('age_restriction', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='EventPlace',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('event', models.ForeignKey(to='events.Event')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='place',
            field=models.ForeignKey(to='events.EventPlace'),
        ),
    ]
