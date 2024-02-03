from django.db import models

from .budget import Budget


class Period(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)

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
