# Generated by Django 3.2.4 on 2021-07-11 14:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('targetApp', '0025_alter_organization_insert_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='insert_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 11, 14, 31, 12, 317068, tzinfo=utc)),
        ),
    ]
