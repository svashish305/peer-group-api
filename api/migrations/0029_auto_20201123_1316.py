# Generated by Django 3.1.2 on 2020-11-23 07:46

import api.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_auto_20201123_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='group_id',
            field=models.ForeignKey(default=api.models.get_default_group, on_delete=django.db.models.deletion.CASCADE, to='api.mygroup'),
        ),
    ]
