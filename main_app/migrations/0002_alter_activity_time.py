# Generated by Django 4.1.1 on 2022-11-01 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='time',
            field=models.TimeField(verbose_name='Time Slot'),
        ),
    ]