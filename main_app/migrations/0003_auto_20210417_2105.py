# Generated by Django 3.2 on 2021-04-17 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_pieces'),
    ]

    operations = [
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Piece Name')),
                ('size', models.CharField(max_length=100)),
                ('boardgame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.boardgame')),
            ],
        ),
        migrations.DeleteModel(
            name='Pieces',
        ),
    ]
