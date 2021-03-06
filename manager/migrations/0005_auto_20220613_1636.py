# Generated by Django 3.2 on 2022-06-13 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_auto_20220613_1619'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='springconfiguration',
            options={'ordering': ('-spring',)},
        ),
        migrations.AddField(
            model_name='springconfiguration',
            name='working_hours',
            field=models.IntegerField(default=1, verbose_name='Horas de Trabajo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='spring',
            name='total_hours',
            field=models.FloatField(blank=True, null=True, verbose_name='Total de Horas'),
        ),
    ]
