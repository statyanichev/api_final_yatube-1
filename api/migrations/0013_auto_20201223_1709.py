# Generated by Django 3.1.4 on 2020-12-23 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20201223_1708'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('following', 'user'), name='unique_followers'),
        ),
    ]
