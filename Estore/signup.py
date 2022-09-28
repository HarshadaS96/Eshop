from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.IntegerField(default=0)
    email = models.EmailField()
    password = models.CharField(max_length=200)
