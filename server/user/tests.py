from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ValidationError

from rest_framework.test import APIClient

from .utils import create_user

User = get_user_model()


class AuthAPITestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            password="test",
            email="example@example.com",
            first_name="Joe",
            last_name="Joe",
        )
        cls.user.password = "test"

    def test_login(self):
        response = self.client.post(
            "/api/auth/login/",
            {"username": self.user.email, "password": self.user.password},
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()["token"])
        self.assertTrue(response.json()["expiry"])


# class CreateUserTestCase(TestCase):
#     def test_successful_creation(self):
#         user = create_user(
#             username="test_user",
#             password="acomplexpassword342@$#",
#             password_confirmation="acomplexpassword342@$#",
#         )
#         self.assertTrue(User.objects.filter(username="test_user").exists())

#     def test_bypass_password_confirmation(self):
#         user = create_user(
#             username="test_user",
#             password="acomplexpassword342@$#",
#             bypass_confirmation_password=True,
#         )

#         self.assertTrue(User.objects.filter(username="test_user").exists())

#     def test_duplicate_creation(self):
#         original_user = create_user(
#             username="test_user",
#             password="acomplexpassword342@$#",
#             bypass_confirmation_password=True,
#         )

#         self.assertRaises(
#             ValueError,
#             create_user,
#             username="test_user",
#             password="acomplexpassword342@$#",
#             bypass_confirmation_password=True,
#         )

#     def test_non_matching_passwords(self):
#         self.assertRaises(ValueError, create_user, username="test_user", password="")


# class CreateUserAPITestCase(TestCase):
#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         cls.user = User.objects.create_user(
#             username="test", password="test", email="example@example.com"
#         )

#     def test_basic(self):
#         authenticated_client = Client()
#         authenticated_client.force_login(self.user)
#         response = authenticated_client.post(
#             "/auth/create/",
#             {
#                 "username": "jess",
#                 "password": "hello",
#                 "password_confirmation": "hello",
#             },
#             content_type="application/json",
#         )
