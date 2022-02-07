from django.db import models

class Plans(models.Model):
    amount = models.IntegerField()
    type = models.TextField()
    description = models.TextField()

class Offers(models.Model):
    description = models.TextField()
    expire = models.DateField()

class Plans_Offers(models.Model):
    plan_id = models.ForeignKey(Plans,on_delete=models.CASCADE)
    offer_id = models.ForeignKey(Offers,on_delete=models.CASCADE)

class Users(models.Model):
    phone = models.CharField(max_length=10)
    previousPlan_id = models.ForeignKey(Plans,on_delete=models.CASCADE)


"""
plans -- offers 
"""




