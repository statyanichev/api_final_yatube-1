# Generated by Django 3.1.4 on 2020-12-23 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_post_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='description',
        ),
        migrations.RemoveField(
            model_name='group',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='post',
            name='group',
        ),
    ]
