# Generated by Django 2.2.7 on 2020-05-23 05:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0004_permissionmodel_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyname', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('landline', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('companyprofile', models.FileField(default='default.jpg', upload_to='resume')),
                ('tin', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('mobile', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('resume', models.FileField(default='default.jpg', upload_to='resume')),
                ('Role', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
