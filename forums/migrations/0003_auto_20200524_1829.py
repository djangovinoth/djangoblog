# Generated by Django 2.2.7 on 2020-05-24 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0002_auto_20200524_1745'),
    ]

    operations = [
        migrations.RenameField(
            model_name='technical',
            old_name='dislikelike',
            new_name='dislike',
        ),
    ]
