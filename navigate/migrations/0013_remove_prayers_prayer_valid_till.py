# Generated by Django 5.1.1 on 2024-10-06 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('navigate', '0012_rename_mosque_name_prayers_mosque_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prayers',
            name='prayer_valid_till',
        ),
    ]
