# Generated by Django 3.2.6 on 2022-07-28 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0005_auto_20220728_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='navelanzadera',
            name='fecha',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='navenotripulada',
            name='fecha',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='navetripulada',
            name='fecha',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
