# Generated by Django 5.1.1 on 2024-10-05 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('navigate', '0010_rename_mosque_name_prayers_mosque_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prayers',
            old_name='mosque_id',
            new_name='mosque_name',
        ),
    ]