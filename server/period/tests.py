from datetime import date

from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient

from budget.models import Budget
from category.models import Category

from .models import Period, PeriodCategory

User = get_user_model()


class PeriodAPITestCase(TestCase):
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

    def test_period_detail_api(self):
        client = APIClient()
        client.force_authenticate(self.user1)
        response = client.get(f"/api/periods/{self.period.id}/")

        assert response.status_code == 200
        assert response.data["id"] == self.period.id

    def test_period_detail_api_unauthorized(self):
        client = APIClient()
        client.force_authenticate(self.user2)
        response = client.get(f"/api/periods/{self.period.id}/")

        assert response.status_code == 403

    def test_period_detail_api_unauthenticated(self):
        client = APIClient()
        response = client.get(f"/api/periods/{self.period.id}/")

        assert response.status_code == 401

    def test_period_delete_api(self):
        client = APIClient()
        client.force_authenticate(self.user1)
        response = client.delete(f"/api/periods/{self.period.id}/")

        assert response.status_code == 204
        assert not Period.objects.filter(id=self.period.id).exists()

    def test_period_delete_api_unauthorized(self):
        client = APIClient()
        client.force_authenticate(self.user2)
        response = client.delete(f"/api/periods/{self.period.id}/")

        assert response.status_code == 403

    def test_period_delete_api_unauthenticated(self):
        client = APIClient()
        response = client.delete(f"/api/periods/{self.period.id}/")

        assert response.status_code == 401

    def test_period_create_api(self):
        client = APIClient()
        client.force_authenticate(self.user1)
        response = client.post(
            f"/api/periods/",
            {"date": "2023-02-03", "budget": self.budget.id},
        )

        assert response.status_code == 201

    def test_period_create_api_unauthorized(self):
        client = APIClient()
        client.force_authenticate(self.user2)
        response = client.post(
            f"/api/periods/",
            {"date": "2023-02-03", "budget": self.budget.id},
        )

        assert response.status_code == 403

    def test_period_create_api_unauthenticated(self):
        client = APIClient()
        response = client.post(
            f"/api/periods/",
            {"date": "2023-02-03", "budget": self.budget.id},
        )

        assert response.status_code == 401

    def test_period_create_api_invalid_budget_id(self):
        client = APIClient()
        client.force_authenticate(self.user1)
        response = client.post(
            "/api/periods/",
            {"date": "2023-02-03", "budget": 99},
        )

        assert response.status_code == 400

    def test_period_update_api(self):
        client = APIClient()
        client.force_authenticate(self.user1)
        response = client.patch(
            f"/api/periods/{self.period.id}/",
            {"start_date": "2023-01-09", "end_date": "2023-01-22"},
        )

        assert response.status_code == 200
        updated_period = Period.objects.get(pk=self.period.id)
        assert updated_period.start_date == date.fromisoformat("2023-01-09")
        assert updated_period.end_date == date.fromisoformat("2023-01-22")

    def test_period_update_api_partial(self):
        client = APIClient()
        client.force_authenticate(self.user1)
        response = client.patch(
            f"/api/periods/{self.period.id}/",
            {"start_date": "2023-01-09"},
        )

        assert response.status_code == 200
        updated_period = Period.objects.get(pk=self.period.id)
        assert updated_period.start_date == date.fromisoformat("2023-01-09")
        assert updated_period.end_date == self.period.end_date

    def test_period_update_api_unauthorized(self):
        client = APIClient()
        client.force_authenticate(self.user2)
        response = client.patch(
            f"/api/periods/{self.period.id}/",
            {"start_date": "2023-01-09", "end_date": "2023-01-22"},
        )

        assert response.status_code == 403

    def test_period_update_api_unauthenticated(self):
        client = APIClient()
        response = client.patch(
            f"/api/periods/{self.period.id}/",
            {"start_date": "2023-01-09", "end_date": "2023-01-22"},
        )

        assert response.status_code == 401

    def test_period_category_list_api(self):
        client = APIClient()
        client.force_authenticate(self.user1)

        response = client.get(f"/api/periods/{self.period.id}/categories/")

        data = response.data
        assert response.status_code == 200
        assert len(data) == 2
        assert data[0] == {
            "id": self.period_category0.id,
            "category": {
                "id": self.category0.id,
                "label": self.category0.label,
                "color": self.category0.color,
                "budget": self.category0.budget.id,
            },
            "value": "45.00",
        }

    def test_period_category_list_api_unauthorized(self):
        client = APIClient()
        client.force_authenticate(self.user2)

        response = client.get(f"/api/periods/{self.period.id}/categories/")

        assert response.status_code == 403

    def test_period_category_list_api_unauthenticated(self):
        client = APIClient()

        response = client.get(f"/api/periods/{self.period.id}/categories/")

        assert response.status_code == 401

    def test_period_category_create_api(self):
        client = APIClient()
        client.force_authenticate(self.user1)

        category = Category.objects.create(
            label="New Category", color="FFDGHR", budget=self.budget
        )

        response = client.post(
            f"/api/periods/{self.period.id}/categories/",
            {"category": category.id, "value": 230.54, "period": self.period.id},
        )

        assert response.status_code == 201

    def test_period_category_create_api_unauthorized(self):
        client = APIClient()
        client.force_authenticate(self.user2)

        category = Category.objects.create(
            label="New Category", color="FFDGHR", budget=self.budget
        )

        response = client.post(
            f"/api/periods/{self.period.id}/categories/",
            {"category": category.id, "value": 230.54, "period": self.period.id},
        )

        assert response.status_code == 403

    def test_period_category_create_api_unauthenticated(self):
        client = APIClient()

        category = Category.objects.create(
            label="New Category", color="FFDGHR", budget=self.budget
        )

        response = client.post(
            f"/api/periods/{self.period.id}/categories/",
            {"category": category.id, "value": 230.54, "period": self.period.id},
        )

        assert response.status_code == 401

    def test_period_category_update_api(self):
        client = APIClient()
        client.force_authenticate(self.user1)

        response = client.patch(
            f"/api/periods/{self.period.id}/categories/{self.period_category0.id}/",
            {"value": "80.00"},
        )

        assert response.status_code == 204

    def test_period_category_update_api_unauthorized(self):
        client = APIClient()
        client.force_authenticate(self.user2)

        response = client.patch(
            f"/api/periods/{self.period.id}/categories/{self.period_category0.id}/",
            {"value": "80.00"},
        )

        assert response.status_code == 403

    def test_period_category_update_api_unauthenticated(self):
        client = APIClient()

        response = client.patch(
            f"/api/periods/{self.period.id}/categories/{self.category0.id}/",
            {"value": "80.00"},
        )

        assert response.status_code == 401

    def test_period_category_delete_api(self):
        client = APIClient()
        client.force_authenticate(self.user1)

        response = client.delete(
            f"/api/periods/{self.period.id}/categories/{self.period_category0.id}/"
        )

        assert response.status_code == 204
        self.assertRaises(
            PeriodCategory.DoesNotExist,
            PeriodCategory.objects.get,
            pk=self.period_category0.id,
        )

    def test_period_category_delete_api_unauthorized(self):
        client = APIClient()
        client.force_authenticate(self.user2)

        response = client.delete(
            f"/api/periods/{self.period.id}/categories/{self.period_category0.id}/"
        )

        assert response.status_code == 403
        assert PeriodCategory.objects.filter(pk=self.period_category0.id).exists()

    def test_period_category_delete_api_unauthenticated(self):
        client = APIClient()

        response = client.delete(
            f"/api/periods/{self.period.id}/categories/{self.period_category0.id}/"
        )

        assert response.status_code == 401
