# Generated by Django 3.1 on 2022-06-30 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0006_auto_20220630_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='spring',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='manager.spring'),
            preserve_default=False,
        ),
    ]
