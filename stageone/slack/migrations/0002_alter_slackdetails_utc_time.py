# Generated by Django 4.2.5 on 2023-09-08 18:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slack', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slackdetails',
            name='utc_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 8, 18, 25, 23, 603496, tzinfo=datetime.timezone.utc)),
        ),
    ]