# Generated by Django 4.1.5 on 2023-02-07 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_movie_description_movie_year_alter_movie_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='hghg', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
