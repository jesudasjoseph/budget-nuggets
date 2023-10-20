from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


def create_user(
    username,
    password,
    password_confirmation=None,
    email=None,
    first_name=None,
    last_name=None,
    bypass_confirmation_password=False,
):
    password_confirmation = (
        password if bypass_confirmation_password else password_confirmation
    )
    new_user = UserCreationForm(
        {
            "username": username,
            "password1": password,
            "password2": password_confirmation,
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
        }
    )
    try:
        user = new_user.save()
        return user
    except ValueError as e:
        raise ValueError("User data invalid!", new_user.errors.as_data())
