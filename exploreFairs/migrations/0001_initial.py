# Generated by Django 5.1 on 2024-09-06 16:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobFair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('event_date', models.DateField()),
                ('location', models.CharField(max_length=255)),
                ('keynote_speaker', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='fairs/images/')),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_fairs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
