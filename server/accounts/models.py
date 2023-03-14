from django.db import models


# Create your models here.
class Account(models.Model):
    account_name = models.CharField(max_length=128)
    created = models.DateField(auto_now_add=True)
