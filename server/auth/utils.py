from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


def create_user(username, password, email=None, first_name=None, last_name=None):
    new_user = UserCreationForm(
        {
            "username": username,
            "password1": password,
            "password2": password,
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
        }
    )
    return new_user.save()
