from django.db import models

from .period import Period


class Category(models.Model):
    label = models.CharField()
    value = models.DecimalField(max_digits=12, decimal_places=2)
    color = models.CharField(max_length=6)
    budget_period = models.ForeignKey(Period, on_delete=models.CASCADE)
