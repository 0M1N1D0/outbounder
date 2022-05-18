# Generated by Django 4.0.4 on 2022-05-18 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Backup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_dist', models.CharField(max_length=20)),
                ('nombres', models.CharField(max_length=200)),
                ('descuento_choice', models.CharField(max_length=10)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('tel_casa', models.CharField(max_length=10)),
                ('tel_cel', models.CharField(max_length=10)),
                ('estado', models.CharField(max_length=100)),
                ('centro_alta', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('fecha_ultima_compra', models.DateField()),
                ('meses_sin_compra', models.IntegerField()),
                ('fecha_alta', models.DateField()),
                ('sexo', models.CharField(max_length=2)),
                ('fecha_nacimiento', models.DateField()),
                ('total_puntos', models.IntegerField()),
                ('campania', models.CharField(max_length=200)),
                ('pais', models.CharField(max_length=200)),
                ('cedi', models.CharField(max_length=200)),
                ('registro_no_exi', models.CharField(max_length=200)),
                ('registro_exi', models.CharField(max_length=200)),
                ('comentario', models.TextField()),
                ('remarcar', models.BooleanField()),
                ('ultima_interaccion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Campania',
            fields=[
                ('nombre', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name': 'Campaña',
                'verbose_name_plural': 'Campañas',
            },
        ),
        migrations.CreateModel(
            name='Cedi',
            fields=[
                ('nombre', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('num_dist', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Número de distribuidor')),
                ('nombre', models.CharField(max_length=200)),
                ('descuento_choice', models.CharField(choices=[('20', '20'), ('25', '25'), ('30', '30'), ('35', '35'), ('40', '40')], default='20', max_length=10)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('tel_casa', models.CharField(max_length=10)),
                ('tel_cel', models.CharField(max_length=10)),
                ('pais', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('centro_alta', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('fecha_ultima_compra', models.DateField()),
                ('meses_sin_compra', models.IntegerField()),
                ('fecha_alta', models.DateField()),
                ('sexo', models.CharField(choices=[('M', 'M'), ('F', 'F')], default='M', max_length=2)),
                ('fecha_nacimiento', models.DateField()),
                ('total_puntos', models.IntegerField()),
                ('campania', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campanias.campania', verbose_name='campaña')),
                ('cedis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campanias.cedi', verbose_name='cedis')),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('nombre', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'País',
                'verbose_name_plural': 'Países',
            },
        ),
        migrations.CreateModel(
            name='RegistroExitoso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon', models.CharField(max_length=300)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Registro Exitoso',
                'verbose_name_plural': 'Registros Exitosos',
            },
        ),
        migrations.CreateModel(
            name='RegistroNoExitoso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon', models.CharField(max_length=300)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Registro No Exitoso',
                'verbose_name_plural': 'Registros No Exitosos',
            },
        ),
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
                ('remarcar', models.BooleanField(default=True)),
                ('fecha_primer_contacto', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('ultima_interaccion', models.DateTimeField(auto_now=True)),
                ('contacto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campanias.contacto')),
                ('registro_exi', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='campanias.registroexitoso')),
                ('registro_no_exi', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='campanias.registronoexitoso')),
            ],
        ),
        migrations.AddField(
            model_name='cedi',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campanias.pais'),
        ),
        migrations.AddField(
            model_name='campania',
            name='cedis',
            field=models.ManyToManyField(to='campanias.cedi'),
        ),
    ]
