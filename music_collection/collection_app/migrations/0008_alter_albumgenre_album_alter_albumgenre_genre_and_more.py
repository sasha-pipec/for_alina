# Generated by Django 4.2 on 2023-06-14 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection_app', '0007_alter_tracks_album_alter_tracks_audio_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumgenre',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collection_app.albums'),
        ),
        migrations.AlterField(
            model_name='albumgenre',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collection_app.genres'),
        ),
        migrations.AlterField(
            model_name='artistalbum',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collection_app.albums'),
        ),
        migrations.AlterField(
            model_name='artistalbum',
            name='artist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collection_app.artists'),
        ),
        migrations.AlterField(
            model_name='trackalbum',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collection_app.albums'),
        ),
        migrations.AlterField(
            model_name='trackalbum',
            name='artist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collection_app.artists'),
        ),
        migrations.AlterField(
            model_name='trackalbum',
            name='track',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collection_app.tracks'),
        ),
        migrations.AlterField(
            model_name='trackclient',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collection_app.client'),
        ),
        migrations.AlterField(
            model_name='trackclient',
            name='track',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collection_app.tracks'),
        ),
        migrations.AlterField(
            model_name='trackgenre',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collection_app.genres'),
        ),
        migrations.AlterField(
            model_name='trackgenre',
            name='track',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collection_app.tracks'),
        ),
    ]
