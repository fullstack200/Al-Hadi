# Generated by Django 5.1.1 on 2024-10-04 14:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigate', '0006_alter_prayers_azaan_time_alter_prayers_prayer_time_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mosques',
            name='mosqueAdmin_id',
        ),
        migrations.AddField(
            model_name='mosques',
            name='mosqueAdmin',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='MosqueAdmin',
        ),
    ]
