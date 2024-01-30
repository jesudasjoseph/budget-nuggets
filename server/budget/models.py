from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class BudgetRole(models.Model):
    id = models.CharField(primary_key=True)
    name = models.CharField()
    description = models.CharField()


class Budget(models.Model):
    ANNUAL = "AN"
    MONTHLY = "MN"
    BI_WEEKLY = "BW"
    WEEKLY = "W"
    EVENT = "EV"

    TYPE_CHOICES = [
        (ANNUAL, "Annual"),
        (MONTHLY, "Monthly"),
        (BI_WEEKLY, "Biweekly"),
        (WEEKLY, "Weekly"),
        (EVENT, "Event"),
    ]

    name = models.CharField()
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default=MONTHLY)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="budget_owner"
    )
    users = models.ManyToManyField(
        User, through="BudgetUser", through_fields=("budget", "user")
    )


class BudgetUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(BudgetRole, on_delete=models.CASCADE)
    budget = models.ForeignKey(
        Budget, on_delete=models.CASCADE, related_name="user_role"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "role", "budget"], name="user unique budget roles"
            )
        ]


class BudgetPeriod(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["start_date", "end_date", "budget"], name="unique budget period"
            )
        ]


class BudgetCategory(models.Model):
    label = models.CharField()
    value = models.DecimalField(max_digits=12, decimal_places=2)
    color = models.CharField(max_length=6)
    budget_period = models.ForeignKey(BudgetPeriod, on_delete=models.CASCADE)
