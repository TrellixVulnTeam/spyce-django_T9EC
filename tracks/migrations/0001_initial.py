# Generated by Django 3.0.3 on 2020-04-27 10:18

from django.db import migrations, models
import tracks.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('bpm', models.IntegerField()),
                ('mp3_price', models.FloatField()),
                ('wav_price', models.FloatField()),
                ('key', models.CharField(default='G#', max_length=7)),
                ('tags', models.CharField(max_length=256, null=True)),
                ('in_cart', models.BooleanField(default=False)),
                ('track_status', models.CharField(default='', max_length=20)),
                ('selected_type', models.CharField(default='mp3', max_length=7)),
                ('artwork', models.ImageField(blank=True, null=True, upload_to=tracks.models.artwork_path)),
                ('sample_audio', models.FileField(upload_to=tracks.models.sample_audio_path)),
                ('mp3', models.FileField(upload_to=tracks.models.mp3_path)),
                ('wav', models.FileField(upload_to=tracks.models.wav_path)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]