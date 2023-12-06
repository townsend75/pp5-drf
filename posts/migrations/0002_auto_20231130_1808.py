# Generated by Django 3.2.23 on 2023-11-30 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='rating_average',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='review_count',
            field=models.IntegerField(default=0),
        ),
    ]