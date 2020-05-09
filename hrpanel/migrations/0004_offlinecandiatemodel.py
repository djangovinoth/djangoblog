# Generated by Django 2.2.7 on 2020-05-08 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hrpanel', '0003_technicalteammodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfflineCandiateModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offlinecandiate', models.CharField(blank=True, max_length=100, null=True)),
                ('uploadresume', models.CharField(blank=True, max_length=100, null=True)),
                ('phonenumber', models.CharField(blank=True, max_length=100, null=True)),
                ('candiateemailid', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offlineusermodel', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
