from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient

from ..models import Budget
from ..serializers import BudgetDetailSerializer

User = get_user_model()


class BudgetAPITestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user1 = User.objects.create_user(email="jess@example.com")
        cls.user2 = User.objects.create_user(email="bob@example.com")

        cls.budget = Budget(name="Test Budget", type=Budget.ANNUAL, owner=cls.user1)
        cls.budget.save()

        cls.budget1 = Budget(
            name="Another Budget", type=Budget.BI_WEEKLY, owner=cls.user1
        )
        cls.budget1.save()

        cls.budget2 = Budget(name="Last Budget", type=Budget.EVENT, owner=cls.user2)
        cls.budget2.save()

    def test_budget_detail_api(self):
        client = APIClient()
        client.force_authenticate(self.user1)
        response = client.get(f"/api/budget/{self.budget.id}/")

        assert response.status_code == 200
        assert response.data["id"] == self.budget.id

    def test_budget_detail_api_unauthorized(self):
        client = APIClient()
        client.force_authenticate(self.user2)
        response = client.get(f"/api/budget/{self.budget.id}/")

        assert response.status_code == 403

    def test_budget_detail_api_unauthenticated(self):
        client = APIClient()
        response = client.get(f"/api/budget/{self.budget.id}/")

        assert response.status_code == 401

    def test_budget_delete_api(self):
        client = APIClient()
        client.force_authenticate(self.user1)
        response = client.delete(f"/api/budget/{self.budget.id}/delete/")

        assert response.status_code == 204
        assert not Budget.objects.filter(id=self.budget.id).exists()

    def test_budget_delete_api_unauthorized(self):
        client = APIClient()
        client.force_authenticate(self.user2)
        response = client.delete(f"/api/budget/{self.budget.id}/delete/")

        assert response.status_code == 403
        assert Budget.objects.filter(id=self.budget.id).exists()

    def test_budget_delete_api_unauthenticated(self):
        client = APIClient()
        response = client.delete(f"/api/budget/{self.budget.id}/delete/")

        assert response.status_code == 401
        assert Budget.objects.filter(id=self.budget.id).exists()

    def test_budget_create_api(self):
        client = APIClient()
        client.force_authenticate(self.user1)
        response = client.post(
            f"/api/budget/create/", {"name": "Test Budget", "type": "W"}
        )

        data = response.data
        assert response.status_code == 201
        budget = Budget.objects.get(id=data["id"])
        assert data == BudgetDetailSerializer(budget).data

    def test_budget_create_api_unauthenticated(self):
        client = APIClient()
        response = client.post(
            f"/api/budget/create/", {"name": "Test Budget", "type": "W"}
        )

        assert response.status_code == 401
        budget = Budget.objects.all().count() == 1

    def test_budget_update_api(self):
        client = APIClient()
        client.force_authenticate(self.user1)
        response = client.patch(
            f"/api/budget/{self.budget.id}/update/", {"name": "Bob Budget"}
        )

        data = response.data
        assert response.status_code == 200
        budget = Budget.objects.get(id=data["id"])
        assert data == BudgetDetailSerializer(budget).data
        assert data["name"] == "Bob Budget"

    def test_budget_update_api_empty_fields(self):
        client = APIClient()
        client.force_authenticate(self.user1)
        response = client.patch(f"/api/budget/{self.budget.id}/update/", {})

        data = response.data
        assert response.status_code == 200
        budget = Budget.objects.get(id=data["id"])
        assert data == BudgetDetailSerializer(budget).data

    def test_budget_update_api_unauthorized(self):
        client = APIClient()
        client.force_authenticate(self.user2)
        response = client.patch(f"/api/budget/{self.budget.id}/update/", {})

        assert response.status_code == 403
        budget = Budget.objects.get(id=self.budget.id)
        assert budget.name == self.budget.name

    def test_budget_update_api_unauthenticated(self):
        client = APIClient()
        response = client.patch(f"/api/budget/{self.budget.id}/update/", {})

        assert response.status_code == 401
        budget = Budget.objects.get(id=self.budget.id)
        assert budget.name == self.budget.name

    def test_budget_list_api(self):
        client = APIClient()
        client.force_authenticate(self.user1)
        response = client.get("/api/budget/")

        data = response.data
        assert response.status_code == 200
        assert len(data) == 2
