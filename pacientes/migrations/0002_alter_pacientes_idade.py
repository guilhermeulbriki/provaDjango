# Generated by Django 3.2.6 on 2021-08-22 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacientes',
            name='idade',
            field=models.IntegerField(),
        ),
    ]