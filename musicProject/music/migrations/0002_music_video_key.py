# Generated by Django 3.0.8 on 2020-07-30 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='video_key',
            field=models.TextField(blank=True),
        ),
    ]
