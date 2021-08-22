# Generated by Django 3.2.6 on 2021-08-22 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medicos', '0001_initial'),
        ('pacientes', '0002_alter_pacientes_idade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('hora', models.CharField(max_length=5)),
                ('convenio', models.CharField(max_length=40)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='medicos.medicos')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pacientes.pacientes')),
            ],
        ),
    ]
