# Generated by Django 4.2.4 on 2024-02-13 04:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IrisGlowApp', '0007_delete_spects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frame',
            name='color',
            field=models.CharField(blank=True, choices=[('Red', 'Red'), ('Blue', 'Blue'), ('Green', 'Green'), ('Black', 'Black'), ('White', 'White')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='frame',
            name='frame_material',
            field=models.CharField(blank=True, choices=[('Metal', 'Metal'), ('Plastic', 'Plastic'), ('Wood', 'Wood'), ('Aluminium', 'Aluminium'), ('Glass', 'Glass')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='frame',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MaxValueValidator(10000)]),
        ),
    ]
