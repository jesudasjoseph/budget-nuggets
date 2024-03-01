from django.db import models
from django.contrib.auth import get_user_model

from budget.models import Budget
from period.models import Period, PeriodCategory

User = get_user_model()


class Transaction(models.Model):
    value = models.DecimalField(max_digits=12, decimal_places=2)
    merchant = models.CharField()
    notes = models.CharField()
    date = models.DateField(auto_now_add=True)

    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    period_categories = models.ManyToManyField(
        PeriodCategory,
        through="TransactionPeriodCategory",
        through_fields=("transaction", "period_category"),
    )


class TransactionPeriodCategory(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    period_category = models.ForeignKey(PeriodCategory, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["transaction", "period_category", "value"],
                name="unique transactions on period category",
            )
        ]
