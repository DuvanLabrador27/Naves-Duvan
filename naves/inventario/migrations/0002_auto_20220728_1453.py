# Generated by Django 3.2.6 on 2022-07-28 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navelanzadera',
            name='fecha',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='navenotripulada',
            name='fecha',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='navetripulada',
            name='fecha',
            field=models.DateTimeField(),
        ),
    ]
