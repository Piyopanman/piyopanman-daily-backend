# Generated by Django 2.2.16 on 2021-01-20 06:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily', '0010_auto_20210116_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 20, 15, 33, 37, 656452)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
    ]
