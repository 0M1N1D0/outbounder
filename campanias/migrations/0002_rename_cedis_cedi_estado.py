# Generated by Django 4.0.4 on 2022-05-06 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campanias', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cedi',
            old_name='cedis',
            new_name='estado',
        ),
    ]
