# Generated by Django 2.2.13 on 2020-07-09 09:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventtitel', models.CharField(max_length=200)),
                ('beschreibung', models.TextField()),
                ('veranstaltungsort', models.CharField(max_length=100)),
                ('published_date2', models.DateTimeField(blank=True, null=True)),
                ('veranstaltungsdatum', models.DateField(default='')),
                ('uhrzeit', models.TimeField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Kontakt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('nachricht', models.TextField()),
                ('created_on_day', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created_on_day'],
            },
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='titel',
        ),
        migrations.AddField(
            model_name='post',
            name='alter',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='bild',
            field=models.ImageField(blank=True, default='default.PNG', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='ort',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('kommentartext', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Post')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
