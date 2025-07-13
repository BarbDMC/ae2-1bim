from django.db import migrations

def cargar_datos_iniciales(apps, schema_editor):
    ParqueNatural = apps.get_model('parque', 'ParqueNatural')
    GuiaTuristico = apps.get_model('parque', 'GuiaTuristico')
    Recorrido = apps.get_model('parque', 'Recorrido')

    parque1 = ParqueNatural.objects.create(
        nombre="Parque Nacional Yasuní",
        ubicacion="Orellana",
        area_km2=9820.00
    )

    parque2 = ParqueNatural.objects.create(
        nombre="Parque Nacional Cajas",
        ubicacion="Azuay",
        area_km2=285.44
    )

    guia1 = GuiaTuristico.objects.create(
        cedula="0102030405",
        nombres="Carlos",
        apellidos="Pérez",
        experiencia=5,
        parque=parque1
    )

    guia2 = GuiaTuristico.objects.create(
        cedula="0911121314",
        nombres="Ana",
        apellidos="Loja",
        experiencia=8,
        parque=parque2
    )

    Recorrido.objects.create(
        nombre="Sendero Tucán",
        duracion_horas=2.5,
        costo=10.00,
        guia=guia1
    )

    Recorrido.objects.create(
        nombre="Laguna Llaviucu",
        duracion_horas=3.0,
        costo=15.00,
        guia=guia2
    )

class Migration(migrations.Migration):

    dependencies = [
        ('parque', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(cargar_datos_iniciales),
    ]
