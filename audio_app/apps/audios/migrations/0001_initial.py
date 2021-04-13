# Generated by Django 3.2 on 2021-04-11 14:10

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AudioTrack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('duration', models.IntegerField(default=0)),
                ('uploaded_time', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AudioBook',
            fields=[
                ('audiotrack_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='audios.audiotrack')),
                ('book_name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('narrator', models.CharField(max_length=100)),
            ],
            bases=('audios.audiotrack',),
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('audiotrack_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='audios.audiotrack')),
                ('host', models.CharField(max_length=100)),
                ('participants', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, null=True, size=None)),
            ],
            bases=('audios.audiotrack',),
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('audiotrack_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='audios.audiotrack')),
                ('artist_name', models.CharField(max_length=100)),
            ],
            bases=('audios.audiotrack',),
        ),
    ]