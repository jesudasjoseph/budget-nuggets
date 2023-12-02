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

    users = models.ManyToManyField(
        User, through="BudgetUsers", through_fields=("budget", "user")
    )
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default=MONTHLY)


class BudgetUsers(models.Model):
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


class BudgetPeriods(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
