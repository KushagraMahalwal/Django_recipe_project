# Generated by Django 4.2.3 on 2023-08-03 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='recipe_desciption',
            new_name='receipe_description',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='recipe_image',
            new_name='receipe_image',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='recipe_name',
            new_name='receipe_name',
        ),
    ]
