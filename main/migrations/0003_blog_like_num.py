# Generated by Django 3.0.6 on 2020-07-28 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_portfolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='like_num',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
