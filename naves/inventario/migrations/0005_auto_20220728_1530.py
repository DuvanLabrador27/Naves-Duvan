# Generated by Django 3.2.6 on 2022-07-28 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_auto_20220728_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='navelanzadera',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='navenotripulada',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='navetripulada',
            name='fecha',
        ),
    ]
