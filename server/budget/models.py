from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class BudgetRole(models.Model):
    id = models.CharField(primary_key=True)
    name = models.CharField()
    description = models.CharField()


class Budget(models.Model):
    users = models.ManyToManyField(
        User, through="BudgetUsers", through_fields=("budget", "user")
    )


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
