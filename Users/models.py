from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=128)

class Admin(models.Model):
    name = models.CharField(max_length=150)
    type = models.TextField()
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=254)



