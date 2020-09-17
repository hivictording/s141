# Generated by Django 2.2 on 2019-05-02 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_auto_20190428_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='name',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='applications',
            name='platform',
            field=models.CharField(choices=[('RH73', 'Red Hat 7.3'), ('W2016', 'Windows Server 2016'), ('W2013', 'Windows Server 2013'), ('U1804', 'Ubuntu Server 18.04'), ('U1604', 'Ubuntu Server 16.04')], default='W2016', max_length=5),
        ),
        migrations.AlterField(
            model_name='hosts',
            name='name',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
    ]
