# Generated by Django 4.2.3 on 2023-09-23 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
