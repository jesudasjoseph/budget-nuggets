from django.db import models

from budget.models import Budget


class Period(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["start_date", "end_date", "budget"], name="unique budget period"
            )
        ]
