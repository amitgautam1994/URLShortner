# Generated by Django 4.2.5 on 2023-10-07 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshort', '0002_shorturl_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]