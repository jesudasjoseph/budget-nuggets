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

        cls.category = Category(label="Savings", color="FFFFFF", budget=cls.budget)
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

    def test_category_create_api(self):
        client = APIClient()
        client.force_authenticate(self.user1)

        category_data = {
            "label": "Savings",
            "color": "123ABC",
            "budget": self.budget.id,
        }

        response = client.post(
            f"/api/category/create/",
            category_data,
        )

        assert response.status_code == 201
        del response.data["id"]
        assert response.data == category_data

    def test_category_create_api_unauthorized(self):
        client = APIClient()
        client.force_authenticate(self.user2)

        category_data = {
            "label": "Savings",
            "color": "123ABC",
            "budget": self.budget.id,
        }

        response = client.post(
            f"/api/category/create/",
            category_data,
        )

        assert response.status_code == 403

    def test_category_create_api_unauthenticated(self):
        client = APIClient()

        category_data = {
            "label": "Savings",
            "color": "123ABC",
            "budget": self.budget.id,
        }

        response = client.post(
            f"/api/category/create/",
            category_data,
        )

        assert response.status_code == 401
