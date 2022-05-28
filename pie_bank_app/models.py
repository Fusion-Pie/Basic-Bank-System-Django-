from datetime import datetime
import email
from email import message
from pyexpat import model
from re import T
from statistics import mode
from django.db import models
from django.contrib.auth.models import *
import datetime as dt

# Create your models here.
class Contact(models.Model):
    # Here automatically field named is created which will be the primary key
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50)
    message = models.TextField()
    date = models.DateField()

    # This function changes the name of object created during the submission of form
    # and set it to the name which you are returing 
    
    # As in this case am returning name + email so it will show like 'Piyush kbsf@mbsf'
    # You can also set it to only name or email or anything you want

    def __str__(self) -> str:
        return self.name + ' ' + str(self.id)


class Bank_user(models.Model):
    Customer_id = models.IntegerField(models.ForeignKey(User, on_delete=models.CASCADE))
    IFSC = models.CharField(max_length=10, primary_key=True)
    Balance = models.FloatField(null=True)    

    def __str__(self) -> str:
        return self.IFSC

class Transction(models.Model):
    Transaction_from = models.CharField(models.ForeignKey(Bank_user, on_delete=models.CASCADE), max_length=10)
    Transaction_to = models.CharField(models.ForeignKey(Bank_user, on_delete=models.CASCADE), max_length=10)
    Amount = models.FloatField()
    date = models.DateField()
    status = models.CharField(max_length=10)