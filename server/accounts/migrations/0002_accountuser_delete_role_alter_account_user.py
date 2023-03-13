# Generated by Django 4.1.3 on 2023-03-13 01:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AccountUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("basic", "Basic"),
                            ("owner", "Owner"),
                            ("admin", "Admin"),
                            ("viewer", "Viewer"),
                        ],
                        default="viewer",
                        max_length=16,
                    ),
                ),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.account",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Role",
        ),
        migrations.AlterField(
            model_name="account",
            name="user",
            field=models.ManyToManyField(
                through="accounts.AccountUser", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
