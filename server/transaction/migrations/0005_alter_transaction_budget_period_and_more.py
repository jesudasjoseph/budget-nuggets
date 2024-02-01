# Generated by Django 4.2.7 on 2024-01-31 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("category", "0001_initial"),
        ("period", "0001_initial"),
        ("transaction", "0004_transaction_budget"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="budget_period",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="period.period"
            ),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="category",
            field=models.ManyToManyField(
                through="transaction.TransactionCategory", to="category.category"
            ),
        ),
        migrations.AlterField(
            model_name="transactioncategory",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="category.category"
            ),
        ),
    ]
