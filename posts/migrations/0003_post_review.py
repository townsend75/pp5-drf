# Generated by Django 3.2.23 on 2023-11-30 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20231130_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='review',
            field=models.IntegerField(choices=[(0, 'Zero'), (1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')], default=1),
        ),
    ]
