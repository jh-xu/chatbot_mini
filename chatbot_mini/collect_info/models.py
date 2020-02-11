from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class users(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    c_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['c_time']

class Records(models.Model):
    name = models.CharField(max_length=128)
    truck_mark = models.CharField(max_length=100)
    truck_model = models.CharField(max_length=100)
    truck_nb = models.IntegerField()
    #created_time = models.DateTimeField()  