# Generated by Django 4.1 on 2022-10-10 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_publicaciones_descripcion_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Gatos',
        ),
        migrations.RemoveField(
            model_name='masinformacion',
            name='user',
        ),
        migrations.DeleteModel(
            name='Perros',
        ),
        migrations.DeleteModel(
            name='Usuarios',
        ),
        migrations.DeleteModel(
            name='MasInformacion',
        ),
    ]