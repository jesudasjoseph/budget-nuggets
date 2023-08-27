from django.test import TestCase
from django.contrib.auth.models import User


# Create your tests here.
class AuthAPITests(TestCase):
    def setUp(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(
            username="test", password="test", email="example@example.com"
        )
        cls.user.password = "test"

    def test_login(cls):
        response = cls.client.post(
            "/auth/login/",
            {"username": cls.user.username, "password": cls.user.password},
        )
        cls.assertEqual(response.status_code, 200)
        cls.assertTrue(response.json()["token"])
        cls.assertTrue(response.json()["expiry"])

    def test_logout(cls):
        response = cls.client.post(
            "/auth/login/",
            {"username": cls.user.username, "password": cls.user.password},
        )

        token = response.json()["token"]

        test_response = cls.client.post(
            "/auth/logout/",
            content_type="application/json",
            headers={
                "Authorization": "Token " + token,
            },
        )

        cls.assertEqual(test_response.status_code, 204)

    def test_logoutall(cls):
        response = cls.client.post(
            "/auth/login/",
            {"username": cls.user.username, "password": cls.user.password},
        )
        response1 = cls.client.post(
            "/auth/login/",
            {"username": cls.user.username, "password": cls.user.password},
        )

        token = response.json()["token"]
        token1 = response1.json()["token"]

        test_response = cls.client.post(
            "/auth/logoutall/",
            content_type="application/json",
            headers={"Authorization": "Token " + token},
        )

        cls.assertEqual(test_response.status_code, 204)
