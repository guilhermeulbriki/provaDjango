# Generated by Django 3.2.6 on 2021-08-22 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consultas',
            name='hora',
        ),
    ]