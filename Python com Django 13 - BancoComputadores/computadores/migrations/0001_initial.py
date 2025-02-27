# Generated by Django 5.1.2 on 2025-02-19 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fabricante', models.CharField(max_length=100)),
                ('processador', models.CharField(max_length=100)),
                ('nucleos', models.IntegerField()),
                ('memoria_ram', models.CharField(max_length=50)),
                ('armazenamento', models.CharField(max_length=100)),
                ('placa_video', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
