from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient

from budget.models import Budget

from .models import Period
from .serializers import PeriodDetailSerializer

User = get_user_model()


class PeriodAPITestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user1 = User.objects.create_user(email="user1@example.com")
        cls.user2 = User.objects.create_user(email="user2@example.com")

        cls.budget = Budget(name="User1's Budget", type=Budget.MONTHLY, owner=cls.user1)
        cls.budget.save()

        cls.period = Period(
            start_date="2023-01-01", end_date="2023-01-31", budget=cls.budget
        )
        cls.period.save()

    def test_period_detail_api(self):
        client = APIClient()
        client.force_authenticate(self.user1)
        response = client.get(f"/api/period/{self.period.id}/")

        assert response.status_code == 200
        assert response.data["id"] == self.period.id

    def test_period_detail_api_unauthorized(self):
        client = APIClient()
        client.force_authenticate(self.user2)
        response = client.get(f"/api/period/{self.period.id}/")

        assert response.status_code == 403

    def test_period_detail_api_unauthenticated(self):
        client = APIClient()
        response = client.get(f"/api/period/{self.period.id}/")

        assert response.status_code == 401

    def test_period_delete_api(self):
        client = APIClient()
        client.force_authenticate(self.user1)
        response = client.delete(f"/api/period/{self.period.id}/delete/")

        assert response.status_code == 204
        assert not Period.objects.filter(id=self.period.id).exists()

    def test_period_delete_api_unauthorized(self):
        client = APIClient()
        client.force_authenticate(self.user2)
        response = client.delete(f"/api/period/{self.period.id}/delete/")

        assert response.status_code == 403

    def test_period_delete_api_unauthenticated(self):
        client = APIClient()
        response = client.delete(f"/api/period/{self.period.id}/delete/")

        assert response.status_code == 401

    def test_period_create_api(self):
        client = APIClient()
        client.force_authenticate(self.user1)
        response = client.post(
            "/api/period/create/",
            {"start_date": "2023-01-03", "end_date": "2023-01-07", "budget": 1},
        )

        assert response.status_code == 201

    def test_period_create_api_unauthorized(self):
        client = APIClient()
        client.force_authenticate(self.user2)
        response = client.post(
            "/api/period/create/",
            {"start_date": "2023-01-03", "end_date": "2023-01-07", "budget": 1},
        )

        assert response.status_code == 403

    def test_period_create_api_unauthenticated(self):
        client = APIClient()
        response = client.post(
            "/api/period/create/",
            {"start_date": "2023-01-03", "end_date": "2023-01-07", "budget": 1},
        )

        assert response.status_code == 401

    def test_period_create_api_invalid_budget_id(self):
        client = APIClient()
        client.force_authenticate(self.user1)
        response = client.post(
            "/api/period/create/",
            {"start_date": "2023-01-03", "end_date": "2023-01-07", "budget": 99},
        )

        assert response.status_code == 400

    def test_period_update_api(self):
        client = APIClient()
        client.force_authenticate(self.user1)
        response = client.patch(
            f"/api/period/{self.period.id}/update/",
            {"start_date": "2023-01-09", "end_date": "2023-01-22"},
        )

        assert response.status_code == 200
        updated_period = Period.objects.get(pk=self.period.id)
        # finish data asserts
