from django.db import models


# Create your models here.

class Loan(models.Model):
    uid = models.CharField(max_length=60)
    fullName = models.CharField(max_length=60)
    number = models.CharField(max_length=60)
    money = models.CharField(max_length=60)
    toDay = models.CharField(max_length=60)
    returnDay = models.CharField(max_length=60)
    loanType = models.BooleanField()

    def __str__(self):
        return self.name
