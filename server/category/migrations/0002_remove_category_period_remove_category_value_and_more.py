# Generated by Django 4.2.7 on 2024-02-05 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("budget", "0001_initial"),
        ("category", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="period",
        ),
        migrations.RemoveField(
            model_name="category",
            name="value",
        ),
        migrations.AddField(
            model_name="category",
            name="budget",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="budget.budget",
            ),
            preserve_default=False,
        ),
    ]
