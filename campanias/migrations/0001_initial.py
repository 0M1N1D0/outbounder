# Generated by Django 4.0.4 on 2022-05-06 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campania',
            fields=[
                ('nombre', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('nombre', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('codigo_eo', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=200)),
                ('apellido_paterno', models.CharField(max_length=200)),
                ('apellido_materno', models.CharField(max_length=200)),
                ('descuento', models.SmallIntegerField(blank=True, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('telefono', models.BigIntegerField(null=True)),
                ('campania', models.ManyToManyField(to='campanias.campania')),
            ],
        ),
        migrations.CreateModel(
            name='Cedi',
            fields=[
                ('nombre', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('cedis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campanias.estado')),
            ],
        ),
        migrations.AddField(
            model_name='campania',
            name='cedis',
            field=models.ManyToManyField(to='campanias.cedi'),
        ),
    ]
