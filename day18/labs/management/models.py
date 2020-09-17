from django.db import models
from django import forms

# Create your models here.

class Hosts(models.Model):
    name = models.CharField(max_length=15,unique=True)
    ip = models.GenericIPAddressField(protocol='IPv4')
    netmask = models.GenericIPAddressField(protocol='IPv4')
    type = models.CharField(max_length=20)
    owner = models.ForeignKey('Users',on_delete=models.CASCADE)
    location = models.CharField(max_length=15)
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}:{}".format(self.name.title(),self.owner)

    class Meta:
        ordering = ['name']
        get_latest_by = "reg_date"


class Users(models.Model):
    gender_choices = {
        ('M','Male'),
        ('F','Female'),
    }
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=12)
    age = models.IntegerField(default=30)
    gender = models.CharField(max_length=1,choices=gender_choices,default='M')
    role = models.CharField(max_length=10,default='Admin')

    def __str__(self):
        return self.username.title()

class Applications(models.Model):
    platform_choices = {
        ('W2016','Windows Server 2016'),
        ('W2013', 'Windows Server 2013'),
        ('U1604', 'Ubuntu Server 16.04'),
        ('U1804', 'Ubuntu Server 18.04'),
        ('RH73', 'Red Hat 7.3'),
    }
    name = models.CharField(max_length=15,unique=True)
    owner = models.ForeignKey(to='Users',on_delete=models.CASCADE)
    platform = models.CharField(max_length=5,choices=platform_choices,default='W2016')
    host = models.ManyToManyField('Hosts')

    class Meta:
        # 降序
        ordering = ['-name']

class ApplicationsnForm(forms.ModelForm):
    class Meta:
        model = Applications
        fields = '__all__'
