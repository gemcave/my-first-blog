# -*- coding: utf-8 -*-
# coding: utf-8

from django.db import models
from django.utils import timezone

# Create your models here.
class Order(models.Model):
    author = models.ForeignKey('auth.User')
    textDep = models.TextField()
    textDest = models.TextField()
    truckType = models.CharField(max_length = 35, default = 'Грузовик1')
    created_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return "Пункт назначения: "+self.textDest+" Пункт отправления: "+self.textDep