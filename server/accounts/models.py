from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Account(models.Model):
    user = models.ManyToManyField(User, through="AccountUser")
    account_name = models.CharField(max_length=128)
    created = models.DateField(auto_now_add=True)


class AccountUser(models.Model):
    Basic = "basic"
    Owner = "owner"
    Admin = "admin"
    Viewer = "viewer"

    Roles = [(Basic, "Basic"), (Owner, "Owner"), (Admin, "Admin"), (Viewer, "Viewer")]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    role = models.CharField(max_length=16, choices=Roles, default=Viewer)
