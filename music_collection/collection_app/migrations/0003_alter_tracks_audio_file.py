# Generated by Django 4.2 on 2023-06-14 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection_app', '0002_client_money'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracks',
            name='audio_file',
            field=models.FileField(blank=True, upload_to='static/audio_files/'),
        ),
    ]
