# Generated by Django 3.1.6 on 2021-02-15 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='likes',
            field=models.BigIntegerField(default=0),
        ),
    ]
