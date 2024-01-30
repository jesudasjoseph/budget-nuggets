# Generated by Django 4.2.7 on 2024-01-30 06:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("budget", "0006_rename_budgetperiods_budgetperiod_and_more"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="budgetperiod",
            constraint=models.UniqueConstraint(
                fields=("start_date", "end_date", "budget"), name="unique budget period"
            ),
        ),
    ]
