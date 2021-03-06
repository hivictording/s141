# Generated by Django 2.2 on 2019-04-28 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_auto_20190428_0950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('platform', models.CharField(choices=[('W2016', 'Windows Server 2016'), ('U1804', 'Ubuntu Server 18.04'), ('U1604', 'Ubuntu Server 16.04'), ('RH73', 'Red Hat 7.3'), ('W2013', 'Windows Server 2013')], default='W2016', max_length=5)),
                ('host', models.ManyToManyField(to='management.Hosts')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Users')),
            ],
        ),
        migrations.DeleteModel(
            name='Application',
        ),
    ]
