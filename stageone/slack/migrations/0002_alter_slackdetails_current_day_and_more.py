# Generated by Django 4.2.5 on 2023-09-09 13:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slack', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slackdetails',
            name='current_day',
            field=models.DateField(default=datetime.datetime(2023, 9, 9, 13, 11, 2, 4765, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='slackdetails',
            name='status_code',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='slackdetails',
            name='utc_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 9, 13, 11, 2, 4794, tzinfo=datetime.timezone.utc)),
        ),
    ]