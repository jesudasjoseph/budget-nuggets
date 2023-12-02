# Generated by Django 4.2.7 on 2023-12-02 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("budget", "0002_budgetperiods"),
    ]

    operations = [
        migrations.AlterField(
            model_name="budgetusers",
            name="budget",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_role",
                to="budget.budget",
            ),
        ),
    ]
