# Generated by Django 3.2.23 on 2023-11-30 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]