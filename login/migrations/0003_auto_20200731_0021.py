# Generated by Django 3.0.6 on 2020-07-30 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_account_like_blog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='like_blog',
            new_name='like_blogs',
        ),
    ]
