# Generated by Django 2.2.13 on 2020-06-15 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text2',
            field=models.TextField(default='place'),
            preserve_default=False,
        ),
    ]
