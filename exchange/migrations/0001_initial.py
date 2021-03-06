# Generated by Django 3.2.9 on 2022-01-07 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('Link', models.URLField()),
                ('usuario', models.CharField(max_length=50)),
                ('senha', models.CharField(max_length=50)),
                ('anotacoes', models.TextField(blank=True, max_length=500)),
                ('tipo', models.CharField(choices=[('C', 'Compra/Venda'), ('S', 'Stake')], max_length=1)),
            ],
        ),
    ]
