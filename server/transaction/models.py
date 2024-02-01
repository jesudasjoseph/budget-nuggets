from django.db import models

from django.contrib.auth import get_user_model

from budget.models import Budget
from category.models import Category
from period.models import Period

User = get_user_model()


class Transaction(models.Model):
    value = models.DecimalField(max_digits=12, decimal_places=2)
    merchant = models.CharField()
    notes = models.CharField()
    date = models.DateField(auto_now_add=True)

    category = models.ManyToManyField(
        Category,
        through="TransactionCategory",
        through_fields=("transaction", "category"),
    )
    budget_period = models.ForeignKey(Period, on_delete=models.CASCADE)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class TransactionCategory(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    partial_value = models.DecimalField(max_digits=12, decimal_places=2)
