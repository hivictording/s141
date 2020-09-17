# Generated by Django 2.2 on 2019-04-27 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_auto_20190426_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='age',
            field=models.IntegerField(default=30),
        ),
        migrations.AddField(
            model_name='users',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='M', max_length=1),
        ),
        migrations.AddField(
            model_name='users',
            name='role',
            field=models.CharField(default='Admin', max_length=10),
        ),
    ]
