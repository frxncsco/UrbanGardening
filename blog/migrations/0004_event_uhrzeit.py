# Generated by Django 2.2.13 on 2020-07-05 16:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='uhrzeit',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
