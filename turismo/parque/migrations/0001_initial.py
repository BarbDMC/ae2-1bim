# Generated by Django 5.2.4 on 2025-07-12 18:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParqueNatural',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ubicacion', models.CharField(max_length=150)),
                ('area_km2', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='GuiaTuristico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=10, unique=True)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('experiencia', models.IntegerField()),
                ('parque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parque.parquenatural')),
            ],
        ),
        migrations.CreateModel(
            name='Recorrido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('duracion_horas', models.DecimalField(decimal_places=2, max_digits=4)),
                ('costo', models.DecimalField(decimal_places=2, max_digits=6)),
                ('guia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parque.guiaturistico')),
            ],
        ),
    ]
