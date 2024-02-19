from django.db import models

from budget.models import Budget


class Category(models.Model):
    label = models.CharField()
    color = models.CharField(max_length=7, null=True)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
