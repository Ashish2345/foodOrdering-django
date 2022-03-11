
from typing import Tuple
from django.db import models

from django.contrib.auth.models import User
from deliverFood.models import Food_Items

# Create your models here.


class Order(models.Model):
    status = (
        ("New","New"),
        ("Accepted","Accepted"),
        ("Completed","Completed"),
        ("Cancelled","Cancelled")

    )

    user= models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    order_number = models.CharField(max_length=50)
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    ordered_Food = models
    order_total = models.FloatField()
    order_note = models.TextField(blank=True)
    status = models.CharField(choices=status, max_length=50, blank="New")
    ip = models.CharField(blank=True, max_length=50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.first_name + "" + self.last_name
    


