# Generated by Django 4.1.5 on 2023-01-26 09:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0007_alter_mensajes_fecha_mensaje_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensajes',
            name='fecha_mensaje',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 26, 6, 19, 3, 197024)),
        ),
        migrations.AlterField(
            model_name='sala_chat',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 26, 6, 19, 3, 196025)),
        ),
        migrations.AlterField(
            model_name='user_sala_chat',
            name='fecha_ingreso',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 26, 6, 19, 3, 197024)),
        ),
    ]
