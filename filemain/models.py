from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.AutoField
    email = models.CharField(max_length=500, default='')
    name = models.CharField(max_length=500, default='')
    profile = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.name
