# Generated by Django 3.2.23 on 2023-12-02 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_post_average_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='average_rating',
        ),
    ]