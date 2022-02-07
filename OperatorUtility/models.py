from django.db import models

class OperatorDetails(models.Model):
    series = models.CharField(max_length=4)
    operatorName = models.CharField(max_length=30)
    state = models.CharField(max_length=100)
    def __str__(self):
        return self.operatorName