# Generated by Django 3.2 on 2021-04-21 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20210421_0200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boardgame',
            old_name='gamestore',
            new_name='gamestores',
        ),
    ]
