# Generated by Django 5.0.7 on 2024-09-29 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ferias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tituloFeria', models.CharField(max_length=250)),
                ('descFeria', models.CharField(max_length=1500)),
                ('fechaFeria', models.DateField()),
                ('lugarFeria', models.CharField(max_length=250)),
                ('ponenteFeria', models.CharField(max_length=250)),
                ('imagenFeria', models.ImageField(upload_to='')),
            ],
        ),
    ]