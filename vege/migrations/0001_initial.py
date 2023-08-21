# Generated by Django 4.2.3 on 2023-08-02 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=100)),
                ('recipe_desciption', models.TextField()),
                ('recipe_image', models.ImageField(upload_to='recipe')),
            ],
        ),
    ]
