# Generated by Django 2.2.4 on 2019-09-25 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='poster_url',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
