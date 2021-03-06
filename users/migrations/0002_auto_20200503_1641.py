# Generated by Django 2.2.7 on 2020-05-03 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permissionmodel',
            name='company',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='permissionmodel',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='permissionmodel',
            name='role',
            field=models.CharField(choices=[('Employee', 'S'), ('Employer', 'E')], max_length=100),
        ),
    ]
