# Generated by Django 4.1.5 on 2023-01-25 02:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensajes',
            name='fecha_mensaje',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 24, 23, 9, 12, 786769)),
        ),
    ]
