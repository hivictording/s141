# Generated by Django 2.2 on 2019-04-26 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hosts',
            old_name='owner_id',
            new_name='owner',
        ),
    ]