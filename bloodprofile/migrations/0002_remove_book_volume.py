# Generated by Django 2.2.6 on 2019-11-02 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloodprofile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='volume',
        ),
    ]
