# Generated by Django 3.2.9 on 2022-01-11 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coinmarketcap', '0003_auto_20220111_1052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coinmarketcap',
            name='initialized',
        ),
        migrations.AlterField(
            model_name='coinmarketcap',
            name='circulating_supply',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='coinmarketcap',
            name='max_supply',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
