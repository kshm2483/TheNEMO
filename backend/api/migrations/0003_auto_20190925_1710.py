# Generated by Django 2.2.4 on 2019-09-25 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_movie_poster_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='adult',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='backdrop_url',
            field=models.TextField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='overview',
            field=models.TextField(default=False),
            preserve_default=False,
        ),
    ]
