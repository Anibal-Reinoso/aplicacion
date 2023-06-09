# Generated by Django 4.2.1 on 2023-06-20 00:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='fecha_contratacion',
            field=models.DateField(verbose_name=datetime.date(2023, 6, 19)),
        ),
        migrations.CreateModel(
            name='RegistroProfesorEscuela',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.TextField(max_length=200, null=True)),
                ('horas', models.IntegerField(null=True)),
                ('escuela', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='aplicacion.escuela')),
                ('profesor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='aplicacion.profesor')),
            ],
        ),
    ]
