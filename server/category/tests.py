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

        cls.category1 = Category(label="Checking", color="123456", budget=cls.budget)
        cls.category1.save()

    def test_category_detail_api(self):
        client = APIClient()
        client.force_authenticate(self.user1)
        response = client.get(f"/api/categories/{self.category.id}/")

        assert response.status_code == 200
        assert response.data["id"] == self.category.id

    def test_category_detail_api_unauthorized(self):
        client = APIClient()
        client.force_authenticate(self.user2)
        response = client.get(f"/api/categories/{self.category.id}/")

        assert response.status_code == 403

    def test_category_detail_api_unauthenticated(self):
        client = APIClient()
        response = client.get(f"/api/categories/{self.category.id}/")

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
            f"/api/categories/",
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
            f"/api/categories/",
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
            f"/api/categories/",
            category_data,
        )

        assert response.status_code == 401

    def test_category_delete_api(self):
        client = APIClient()
        client.force_authenticate(self.user1)

        response = client.delete(f"/api/categories/{self.category.id}/")

        assert response.status_code == 204
        assert not Category.objects.filter(pk=self.category.id).exists()

    def test_category_delete_api_unauthorized(self):
        client = APIClient()
        client.force_authenticate(self.user2)

        response = client.delete(f"/api/categories/{self.category.id}/")

        assert response.status_code == 403
        assert Category.objects.filter(pk=self.category.id).exists()

    def test_category_delete_api_unauthenticated(self):
        client = APIClient()

        response = client.delete(f"/api/categories/{self.category.id}/")

        assert response.status_code == 401
        assert Category.objects.filter(pk=self.category.id).exists()

    def test_category_update_api(self):
        client = APIClient()
        client.force_authenticate(self.user1)

        response = client.patch(
            f"/api/categories/{self.category.id}/",
            {"label": "Car", "color": "123456"},
        )

        assert response.status_code == 200
        assert response.data["label"] == "Car"
        assert response.data["color"] == "123456"

    def test_category_update_api_unauthorized(self):
        client = APIClient()
        client.force_authenticate(self.user2)

        response = client.patch(
            f"/api/categories/{self.category.id}/",
            {"label": "Car", "color": "123456"},
        )

        assert response.status_code == 403

    def test_category_update_api_unauthenticated(self):
        client = APIClient()

        response = client.patch(
            f"/api/categories/{self.category.id}/",
            {"label": "Car", "color": "123456"},
        )

        assert response.status_code == 401

    def test_category_list_api(self):
        client = APIClient()
        client.force_authenticate(self.user1)
        response = client.get(f"/api/categories/?budget={self.budget.id}")

        assert response.status_code == 200
        assert len(response.data) == 2
