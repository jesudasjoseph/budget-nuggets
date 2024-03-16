from datetime import date

from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient

from budget.models import Budget
from category.models import Category
from period.models import Period, PeriodCategory
from .models import Transaction

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

        cls.category = Category(label="Household Supply", budget=cls.budget)
        cls.category.save()

        cls.category1 = Category(label="Groceries", budget=cls.budget)
        cls.category1.save()

        cls.period_category = PeriodCategory(
            category=cls.category, value=80.00, period=cls.period
        )
        cls.period_category.save()

        cls.period_category1 = PeriodCategory(
            category=cls.category1, value=100.00, period=cls.period
        )
        cls.period_category1.save()

        cls.transaction1 = Transaction(
            value=105,
            merchant="Chick Fil A",
            notes="Some notes",
            date="2024-01-02",
            user=cls.user1,
            budget=cls.budget,
            period=cls.period,
        )
        cls.transaction1.save()

        cls.transaction2 = Transaction(
            value=10.50,
            merchant="Burger King",
            date="2024-01-06",
            user=cls.user1,
            budget=cls.budget,
            period=cls.period,
        )
        cls.transaction2.save()

        cls.transaction3 = Transaction(
            value=5.00,
            merchant="Goodwill",
            notes="Gift for Joe",
            date="2024-01-07",
            user=cls.user1,
            budget=cls.budget,
            period=cls.period,
        )
        cls.transaction3.save()

        cls.transaction4 = Transaction(
            value=80,
            merchant="Del Alma",
            date="2024-01-09",
            user=cls.user1,
            budget=cls.budget,
            period=cls.period,
        )
        cls.transaction4.save()

        cls.transaction5 = Transaction(
            value=35,
            merchant="Comcast",
            notes="Internet Bill",
            date="2024-01-20",
            user=cls.user1,
            budget=cls.budget,
            period=cls.period,
        )
        cls.transaction5.save()

        cls.transaction6 = Transaction(
            value=1000,
            merchant="Rent",
            date="2024-01-21",
            user=cls.user1,
            budget=cls.budget,
            period=cls.period,
        )
        cls.transaction6.save()

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
                "period_categories": [
                    {"period_category": self.period_category.id, "value": 25.00},
                    {"period_category": self.period_category1.id, "value": 25.50},
                ],
            },
            format="json",
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

    def test_transaction_create_api_invalid_period_category_total(self):
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
                "period_categories": [
                    {"period_category": self.period_category.id, "value": 25.00},
                    {"period_category": self.period_category1.id, "value": 20.50},
                ],
            },
            format="json",
        )

        assert response.status_code == 400

    def test_transaction_create_api_invalid_period_category(self):
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
                "period_categories": [
                    {"period_category": "f", "value": 25.00},
                    {"period_category": self.period_category1.id, "value": 25.50},
                ],
            },
            format="json",
        )

        assert response.status_code == 400

    def test_transaction_create_api_no_period_categories(self):
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
            format="json",
        )

        assert response.status_code == 201

    def test_transaction_delete_api(self):
        client = APIClient()
        client.force_authenticate(self.user1)

        response = client.delete(f"/api/transactions/{self.transaction1.id}/")

        assert response.status_code == 204
        self.assertRaises(
            Transaction.DoesNotExist, Transaction.objects.get, pk=self.transaction1.id
        )

    def test_transaction_delete_api_unauthorized(self):
        client = APIClient()
        client.force_authenticate(self.user2)

        response = client.delete(f"/api/transactions/{self.transaction1.id}/")

        assert response.status_code == 403
        assert Transaction.objects.filter(pk=self.transaction1.id).exists()

    def test_transaction_delete_api_unauthenticated(self):
        client = APIClient()

        response = client.delete(f"/api/transactions/{self.transaction1.id}/")

        assert response.status_code == 401
        assert Transaction.objects.filter(pk=self.transaction1.id).exists()

    def test_transaction_delete_api_not_found(self):
        client = APIClient()
        client.force_authenticate(self.user1)
        response = client.delete(f"/api/transactions/999/")

        assert response.status_code == 404
        assert Transaction.objects.filter(pk=self.transaction1.id).exists()

    def test_transaction_list_api(self):
        client = APIClient()
        client.force_authenticate(self.user1)
        response = client.get(
            f"/api/transactions/?budget={self.budget.id}&period={self.period.id}&from_date=2024-01-06&to_date=2024-01-20"
        )

        assert response.status_code == 200
        assert len(response.data) == 4
        assert response.data[0]["id"] == self.transaction2.id
        assert response.data[1]["id"] == self.transaction3.id
        assert response.data[2]["id"] == self.transaction4.id
        assert response.data[3]["id"] == self.transaction5.id

    def test_transaction_list_unauthorized_budget(self):
        client = APIClient()
        client.force_authenticate(self.user1)
        response = client.get(
            f"/api/transactions/?budget={self.budget1.id}&period={self.period.id}"
        )

        assert response.status_code == 403

    def test_transaction_list_unauthorized_period(self):
        client = APIClient()
        client.force_authenticate(self.user1)
        response = client.get(
            f"/api/transactions/?budget={self.budget.id}&period={self.period1.id}"
        )

        assert response.status_code == 403

    def test_transaction_list_unauthenticated(self):
        client = APIClient()
        response = client.get(
            f"/api/transactions/?budget={self.budget.id}&period={self.period.id}"
        )

        assert response.status_code == 401

    def test_transaction_list_missing_budget_param(self):
        client = APIClient()
        client.force_authenticate(self.user1)
        response = client.get(f"/api/transactions/?period={self.period.id}")

        assert response.status_code == 400
