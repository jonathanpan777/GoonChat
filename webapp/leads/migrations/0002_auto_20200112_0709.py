# Generated by Django 3.0.2 on 2020-01-12 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blog',
            new_name='Lead',
        ),
    ]
