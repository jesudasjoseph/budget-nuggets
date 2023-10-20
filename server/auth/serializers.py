from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        required=True,
    )
    password = serializers.CharField(write_only=True, required=True)
    password_confirmation = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "first_name", "last_name"]

    def validate(self, data):
        if data["password"] != data["password_confirmation"]:
            raise serializers.ValidationError({"password": "Passwords do not match!"})


class UserSerializer(serializers.Serializer):
    class Meta:
        modal = User
        fields = ["username", "created"]
