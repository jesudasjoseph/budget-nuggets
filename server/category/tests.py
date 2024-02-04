from datetime import date

from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient

from budget.models import Budget
from period.models import Period

from .models import Category

User = get_user_model()


class CategoryAPITestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user1 = User.objects.create_user(email="user1@example.com")
        cls.user2 = User.objects.create_user(email="user2@example.com")

        cls.budget = Budget(name="User1's Budget", type=Budget.MONTHLY, owner=cls.user1)
        cls.budget.save()

        cls.period = Period(
            start_date=date.fromisoformat("2023-01-01"),
            end_date=date.fromisoformat("2023-01-31"),
            budget=cls.budget,
        )
        cls.period.save()

        cls.category = Category(
            label="Savings", value=4.3, color="FFFFFF", period=cls.period
        )
        cls.category.save()

    def test_category_detail_api(self):
        client = APIClient()
        client.force_authenticate(self.user1)
        response = client.get(f"/api/category/{self.category.id}/")

        assert response.status_code == 200
        assert response.data["id"] == self.category.id

    def test_category_detail_api_unauthorized(self):
        client = APIClient()
        client.force_authenticate(self.user2)
        response = client.get(f"/api/category/{self.category.id}/")

        assert response.status_code == 403

    def test_category_detail_api_unauthenticated(self):
        client = APIClient()
        response = client.get(f"/api/category/{self.category.id}/")

        assert response.status_code == 401
