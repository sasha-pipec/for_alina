# Generated by Django 4.2 on 2023-06-06 15:47

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='created')),
                ('modified', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='modified')),
                ('title', models.CharField(max_length=100)),
                ('year', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2023)])),
                ('category', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name': 'album',
                'verbose_name_plural': 'albums',
                'db_table': '"collection"."album"',
            },
        ),
        migrations.CreateModel(
            name='Tracks',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='created')),
                ('modified', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='modified')),
                ('title', models.CharField(max_length=50)),
                ('audio_file', models.FileField(blank=True, upload_to='audio_files/')),
                ('duration', models.PositiveIntegerField(blank=True, null=True)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2023)])),
                ('country', models.TextField(blank=True)),
                ('rating', models.IntegerField()),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collection_app.albums')),
            ],
            options={
                'verbose_name': 'track',
                'verbose_name_plural': 'tracks',
                'db_table': '"collection"."tracks"',
            },
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='created')),
                ('modified', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='modified')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('tracks', models.ManyToManyField(blank=True, to='collection_app.tracks')),
            ],
            options={
                'verbose_name': 'genre',
                'verbose_name_plural': 'genres',
                'db_table': '"collection"."genre"',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='created')),
                ('modified', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='modified')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('tracks', models.ManyToManyField(blank=True, to='collection_app.tracks')),
            ],
            options={
                'verbose_name': 'client',
                'verbose_name_plural': 'client',
                'db_table': '"collection"."client"',
            },
        ),
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='created')),
                ('modified', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='modified')),
                ('name', models.CharField(max_length=50)),
                ('birth_date', models.DateField(blank=True)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('education', models.TextField(blank=True, max_length=100)),
                ('tracks', models.ManyToManyField(blank=True, to='collection_app.tracks')),
            ],
            options={
                'verbose_name': 'artist',
                'verbose_name_plural': 'artists',
                'db_table': '"collection"."artists"',
            },
        ),
        migrations.AddField(
            model_name='albums',
            name='artist',
            field=models.ManyToManyField(blank=True, to='collection_app.artists'),
        ),
        migrations.AddField(
            model_name='albums',
            name='genres',
            field=models.ManyToManyField(blank=True, to='collection_app.genres'),
        ),
        migrations.CreateModel(
            name='TrackGenre',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='created')),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collection_app.genres')),
                ('track', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collection_app.tracks')),
            ],
            options={
                'db_table': '"collection"."track_genre"',
                'unique_together': {('track', 'genre')},
            },
        ),
        migrations.CreateModel(
            name='TrackClient',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='created')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collection_app.client')),
                ('track', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collection_app.tracks')),
            ],
            options={
                'db_table': '"collection"."track_client"',
                'unique_together': {('track', 'client')},
            },
        ),
        migrations.CreateModel(
            name='TrackAlbum',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='created')),
                ('album', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collection_app.albums')),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collection_app.artists')),
                ('track', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collection_app.tracks')),
            ],
            options={
                'db_table': '"collection"."track_album"',
                'unique_together': {('track', 'album')},
            },
        ),
        migrations.CreateModel(
            name='ArtistAlbum',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='created')),
                ('album', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collection_app.albums')),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collection_app.artists')),
            ],
            options={
                'db_table': '"collection"."artist_album"',
                'unique_together': {('artist', 'album')},
            },
        ),
        migrations.CreateModel(
            name='AlbumGenre',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='created')),
                ('album', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collection_app.albums')),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collection_app.genres')),
            ],
            options={
                'db_table': '"collection"."album_genre"',
                'unique_together': {('album', 'genre')},
            },
        ),
    ]
