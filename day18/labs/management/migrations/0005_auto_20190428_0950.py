# Generated by Django 2.2 on 2019-04-28 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_auto_20190428_0931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='Platform',
        ),
        migrations.AddField(
            model_name='application',
            name='platform',
            field=models.CharField(choices=[('W2016', 'Windows Server 2016'), ('W2013', 'Windows Server 2013'), ('U1804', 'Ubuntu Server 18.04'), ('RH73', 'Red Hat 7.3'), ('U1604', 'Ubuntu Server 16.04')], default='W2016', max_length=5),
        ),
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='M', max_length=1),
        ),
    ]
