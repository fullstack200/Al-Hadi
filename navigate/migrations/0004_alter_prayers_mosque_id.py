# Generated by Django 5.1.1 on 2024-10-03 07:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigate', '0003_prayers_azaan_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prayers',
            name='mosque_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prayers', to='navigate.mosques'),
        ),
    ]
