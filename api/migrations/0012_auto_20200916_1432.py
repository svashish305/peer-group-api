# Generated by Django 3.0.8 on 2020-09-16 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_delete_usergroupmapping'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='grade',
            new_name='rating',
        ),
    ]
