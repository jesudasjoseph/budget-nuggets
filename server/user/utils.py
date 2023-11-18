from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


def create_user(
    email,
    password,
    first_name=None,
    last_name=None,
):
    new_user = User.objects.create_user(email, first_name, last_name, password)

    try:
        new_user.save()
        return new_user
    except ValueError as e:
        raise ValueError("User data invalid!", new_user.errors.as_data())
