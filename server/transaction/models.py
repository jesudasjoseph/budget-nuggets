from django.db import models
from django.contrib.auth import get_user_model

from budget.models import Budget
from period.models import Period
from category.models import Category

User = get_user_model()


class Transaction(models.Model):
    value = models.DecimalField(max_digits=12, decimal_places=2)
    merchant = models.CharField()
    notes = models.CharField()
    date = models.DateField(auto_now_add=True)

    budget = models.ManyToManyField(
        Budget,
        through="TransactionBudget",
        through_fields=("transaction", "budget"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class TransactionBudget(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["transaction", "budget", "period", "category"],
                name="unique transactions on budget",
            )
        ]
