# Generated by Django 3.2 on 2021-04-21 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210417_2105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gamestore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='boardgame',
            name='gamestore',
            field=models.ManyToManyField(to='main_app.Gamestore'),
        ),
    ]
