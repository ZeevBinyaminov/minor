# Generated by Django 4.2.2 on 2023-06-14 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AlgorithmApp', '0003_rename_place_place_loc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='loc',
            new_name='location',
        ),
    ]