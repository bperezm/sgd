# Generated by Django 3.2 on 2022-06-13 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Nombre')),
                ('acronym', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='Siglas')),
                ('start_date', models.DateTimeField(verbose_name='Fecha Inicio')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='Fecha Fin')),
            ],
            options={
                'ordering': ('-start_date',),
            },
        ),
    ]