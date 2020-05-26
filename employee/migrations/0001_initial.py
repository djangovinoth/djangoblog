# Generated by Django 2.2.7 on 2020-05-23 11:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeEduDetailsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institutionname', models.CharField(blank=True, max_length=100, null=True)),
                ('specialization', models.CharField(blank=True, max_length=100, null=True)),
                ('yearofpassing', models.IntegerField(blank=True, null=True)),
                ('score', models.CharField(blank=True, max_length=100, null=True)),
                ('qualification', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employeeedudetailsmodel', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
