# Generated by Django 5.0.7 on 2024-07-28 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_rename_enderecomedico_medico_endereco_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medico',
            old_name='nome',
            new_name='nomeCompleto',
        ),
        migrations.RenameField(
            model_name='paciente',
            old_name='nome',
            new_name='nomeCompleto',
        ),
    ]