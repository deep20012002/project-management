# Generated by Django 5.0.3 on 2024-04-06 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_rename_status_projectmodule_status_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectmodule',
            old_name='status_name',
            new_name='status',
        ),
    ]
