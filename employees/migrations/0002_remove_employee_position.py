# Generated by Django 5.1.2 on 2024-11-04 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='position',
        ),
    ]
