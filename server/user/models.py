from django.db import models
from django.contrib.auth.models import User as AuthUser
from accounts.models import Account


# Create your models here.
class User(models.Model):
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
    account = models.ManyToManyField(Account, through="Accounts")


class Accounts(models.Model):
    Basic = "basic"
    Owner = "owner"
    Admin = "admin"
    Viewer = "viewer"

    Roles = [(Basic, "Basic"), (Owner, "Owner"), (Admin, "Admin"), (Viewer, "Viewer")]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    role = models.CharField(max_length=16, choices=Roles, default=Viewer)
