from datetime import datetime

from django.db import models

from Users.models import Users


class Transaction_Details(models.Model):
    transaction_number = models.CharField(max_length=25)
    transaction_type = models.TextField()
    operator = models.TextField()
    phone = models.CharField(max_length=10)
    user_id = models.ForeignKey(Users,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.now())
