# Generated by Django 2.2 on 2019-05-24 06:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus_admin', '0008_auto_20190524_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='offers',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='offers',
            name='time',
            field=models.TimeField(default=datetime.datetime.now),
        ),
    ]
