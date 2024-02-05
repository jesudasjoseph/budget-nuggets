from django.db import models

from budget.models import Budget
from category.models import Category


class Period(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    categories = models.ManyToManyField(
        Category, through="PeriodCategory", through_fields=("period", "category")
    )

    def label(self):
        "Returns the lebel for this budget period, based on budget type."
        generated_label = self.start_date
        if self.budget.type == Budget.ANNUAL:
            generated_label = self.start_date.year
        elif self.budget.type == Budget.MONTHLY:
            generated_label = self.start_date.strftime("%B")

        return generated_label

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["start_date", "end_date", "budget"], name="unique budget period"
            )
        ]


class PeriodCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=12, decimal_places=2)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["category", "period"], name="category unique to period"
            )
        ]
