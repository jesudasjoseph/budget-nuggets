from django.db import models

from django.contrib.auth import get_user_model

from budget.models import BudgetCategory, BudgetPeriod, Budget

User = get_user_model()


class Transaction(models.Model):
    value = models.DecimalField(max_digits=12, decimal_places=2)
    merchant = models.CharField()
    notes = models.CharField()
    date = models.DateField(auto_now_add=True)

    category = models.ManyToManyField(
        BudgetCategory,
        through="TransactionCategory",
        through_fields=("transaction", "category"),
    )
    budget_period = models.ForeignKey(BudgetPeriod, on_delete=models.CASCADE)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class TransactionCategory(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    category = models.ForeignKey(BudgetCategory, on_delete=models.CASCADE)
    partial_value = models.DecimalField(max_digits=12, decimal_places=2)
