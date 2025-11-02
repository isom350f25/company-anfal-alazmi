from django.db import models

# Create your models here.
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    joined_on = models.DateField()
    phone_number = models.CharField(max_length=15)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name
