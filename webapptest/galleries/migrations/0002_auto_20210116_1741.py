# Generated by Django 3.1.5 on 2021-01-16 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='slug',
            field=models.SlugField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='slug',
            field=models.SlugField(max_length=100, null=True),
        ),
    ]