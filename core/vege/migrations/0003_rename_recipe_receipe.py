# Generated by Django 4.2.3 on 2023-08-03 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0002_rename_recipe_desciption_recipe_receipe_description_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Recipe',
            new_name='Receipe',
        ),
    ]
