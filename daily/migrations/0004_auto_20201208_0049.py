# Generated by Django 3.1.3 on 2020-12-07 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily', '0003_auto_20201208_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily',
            name='first_meet',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='daily',
            name='other',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='daily',
            name='study',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='daily',
            name='summary',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='daily',
            name='univ',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='daily',
            name='wanna_do',
            field=models.TextField(),
        ),
    ]
