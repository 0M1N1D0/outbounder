# Generated by Django 4.0.4 on 2022-05-24 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campanias', '0002_remove_resultado_fecha_modificacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultado',
            name='remarcar',
            field=models.BooleanField(default=False),
        ),
    ]