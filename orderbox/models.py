from django.db import models
from django.utils import timezone

# Create your models here.
class Order(models.Model):
    author = models.ForeignKey('auth.User')
    textDep = models.TextField()
    textDest = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.textDest+" "+self.textDep