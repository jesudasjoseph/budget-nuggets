from datetime import date

from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient

from budget.models import Budget
from category.models import Category

from .models import Period, PeriodCategory

User = get_user_model()


class TransactionAPITestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user1 = User.objects.create_user(email="user1@example.com")
        cls.user2 = User.objects.create_user(email="user2@example.com")

        cls.budget = Budget(name="User1's Budget", type=Budget.MONTHLY, owner=cls.user1)
        cls.budget.save()

        cls.budget1 = Budget(
            name="User2's Budget", type=Budget.MONTHLY, owner=cls.user2
        )
        cls.budget1.save()

        cls.period = Period(
            start_date=date.fromisoformat("2023-01-01"),
            end_date=date.fromisoformat("2023-01-31"),
            budget=cls.budget,
        )
        cls.period.save()

        cls.period1 = Period(
            start_date=date.fromisoformat("2023-01-01"),
            end_date=date.fromisoformat("2023-01-31"),
            budget=cls.budget1,
        )
        cls.period1.save()

        cls.category0 = Category(label="Test 1", budget=cls.budget)
        cls.category0.save()

        cls.category1 = Category(label="Test 2", budget=cls.budget)
        cls.category1.save()

        cls.period_category0 = PeriodCategory.objects.create(
            category=cls.category0, value=45.00, period=cls.period
        )
        cls.period_category1 = PeriodCategory.objects.create(
            category=cls.category1, value=55.00, period=cls.period
        )

    def test_transaction_create_api(self):
        client = APIClient()
        client.force_authenticate(self.user1)
        response = client.post(
            f"/api/transactions/",
            {
                "value": 50.50,
                "merchant": "Sushi",
                "notes": "Some notes",
                "date": "2024-04-09",
                "budget": self.budget.id,
                "period": self.period.id,
            },
        )

        assert response.status_code == 201

    def test_transaction_create_api_unauthorized(self):
        client = APIClient()
        client.force_authenticate(self.user2)
        response = client.post(
            f"/api/transactions/",
            {
                "value": 50.50,
                "merchant": "Sushi",
                "notes": "Some notes",
                "date": "2024-04-09",
                "budget": self.budget.id,
                "period": self.period.id,
            },
        )

        assert response.status_code == 403

    def test_transaction_create_api_unauthenticated(self):
        client = APIClient()
        response = client.post(
            f"/api/transactions/",
            {
                "value": 50.50,
                "merchant": "Sushi",
                "notes": "Some notes",
                "date": "2024-04-09",
                "budget": self.budget.id,
                "period": self.period.id,
            },
        )

        assert response.status_code == 401

    def test_transaction_create_api_invalid_period(self):
        client = APIClient()
        client.force_authenticate(self.user1)
        response = client.post(
            f"/api/transactions/",
            {
                "value": 50.50,
                "merchant": "Sushi",
                "notes": "Some notes",
                "date": "2024-04-09",
                "budget": self.budget.id,
                "period": self.period1.id,
            },
        )

        assert response.status_code == 400
