# Generated by Django 3.0.8 on 2020-09-16 17:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20200916_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='rating',
            field=models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
