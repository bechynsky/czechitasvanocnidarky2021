# Generated by Django 3.2.9 on 2021-11-27 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_vanocnidarky2021', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instituce',
            name='cislo',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='instituce',
            name='psc',
            field=models.IntegerField(),
        ),
    ]