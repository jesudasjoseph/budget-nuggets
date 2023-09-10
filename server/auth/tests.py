from django.test import TestCase
from django.contrib.auth.models import User


# Create your tests here.
class AuthAPITests(TestCase):
    def setUp(self):
        super().setUpClass()
        self.user = User.objects.create_user(
            username="test", password="test", email="example@example.com"
        )
        self.user.password = "test"

    def test_login(self):
        response = self.client.post(
            "/auth/login/",
            {"username": self.user.username, "password": self.user.password},
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()["token"])
        self.assertTrue(response.json()["expiry"])

    def test_logout(self):
        response = self.client.post(
            "/auth/login/",
            {"username": self.user.username, "password": self.user.password},
        )

        token = response.json()["token"]

        test_response = self.client.post(
            "/auth/logout/",
            content_type="application/json",
            headers={
                "Authorization": "Token " + token,
            },
        )

        self.assertEqual(test_response.status_code, 204)

    def test_logoutall(self):
        response = self.client.post(
            "/auth/login/",
            {"username": self.user.username, "password": self.user.password},
        )
        response1 = self.client.post(
            "/auth/login/",
            {"username": self.user.username, "password": self.user.password},
        )

        token = response.json()["token"]
        token1 = response1.json()["token"]

        test_response = self.client.post(
            "/auth/logoutall/",
            content_type="application/json",
            headers={"Authorization": "Token " + token},
        )

        self.assertEqual(test_response.status_code, 204)
