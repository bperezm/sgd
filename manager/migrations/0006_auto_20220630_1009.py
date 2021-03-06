# Generated by Django 3.1 on 2022-06-30 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_auto_20220613_1636'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Nombre')),
                ('ut', models.IntegerField(verbose_name='Horas')),
                ('type', models.CharField(choices=[('E', 'Evolutivo'), ('C', 'Correctivo')], max_length=1, verbose_name='Tipo')),
                ('project_phase', models.CharField(choices=[('C', 'Construcción'), ('A', 'Analisis'), ('P', 'Pruebas')], max_length=1, verbose_name='Fase')),
                ('start_date', models.DateField(verbose_name='Fecha Inicio')),
                ('end_date', models.DateField(verbose_name='Fecha Fin')),
            ],
            options={
                'ordering': ('-end_date',),
            },
        ),
        migrations.AlterField(
            model_name='developer',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='proyect',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='spring',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='springconfiguration',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
