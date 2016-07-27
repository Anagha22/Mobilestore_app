# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('model_name', models.CharField(max_length=300)),
                ('brand_name', models.CharField(max_length=300)),
                ('battery_capacity', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('front_cam', models.FloatField()),
                ('back_cam', models.FloatField()),
                ('ram', models.FloatField()),
                ('screen_size', models.FloatField()),
                ('price', models.FloatField()),
                ('release_data', models.DateTimeField()),
                ('img', models.ImageField(upload_to=b'/mobiles/')),
            ],
        ),
    ]
