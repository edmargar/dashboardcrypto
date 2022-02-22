# Generated by Django 3.2.9 on 2022-01-08 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coinmarketcap', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coinmarketcap',
            name='logo',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='coinmarketcap',
            name='slug',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='coinmarketcap',
            name='symbol',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='coinmarketcap',
            name='url',
            field=models.URLField(blank=True, max_length=100),
        ),
    ]
