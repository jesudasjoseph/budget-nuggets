from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


def create_user(
    email,
    password,
    password_confirmation=None,
    first_name=None,
    last_name=None,
    bypass_confirmation_password=False,
):
    password_confirmation = (
        password if bypass_confirmation_password else password_confirmation
    )
    new_user = User.objects.create_user(email, first_name, last_name)

    try:
        user = new_user.save()
        return user
    except ValueError as e:
        raise ValueError("User data invalid!", new_user.errors.as_data())
