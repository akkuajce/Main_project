# Generated by Django 4.2.4 on 2024-02-10 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IrisGlowApp', '0002_alter_userprofile_country_alter_userprofile_gender_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spects',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('confirm_password', models.CharField(max_length=128)),
            ],
        ),
    ]