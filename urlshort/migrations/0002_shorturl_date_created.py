# Generated by Django 4.2.5 on 2023-10-07 17:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshort', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorturl',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 7, 23, 2, 46, 349849)),
        ),
    ]
