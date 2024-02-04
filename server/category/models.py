from django.db import models

from period.models import Period


class Category(models.Model):
    label = models.CharField()
    value = models.DecimalField(max_digits=12, decimal_places=2)
    color = models.CharField(max_length=6)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)