# Generated by Django 4.2.7 on 2024-07-23 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='updated_on',
        ),
    ]
