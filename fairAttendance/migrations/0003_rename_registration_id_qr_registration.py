# Generated by Django 5.1 on 2024-09-30 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fairAttendance', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qr',
            old_name='registration_id',
            new_name='registration',
        ),
    ]
