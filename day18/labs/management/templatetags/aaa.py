# Author: Victor Ding

# -*- coding: utf-8 -*-

from django import template
from management import models

register = template.Library()

@register.simple_tag
def test(id):
    obj1 = models.Users.objects.filter(id=id).first()
    return obj1.username

@register.filter
def test2(id):
    return models.Users.objects.filter(id=id).first().username