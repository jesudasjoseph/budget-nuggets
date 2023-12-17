from django.contrib.auth import login, authenticate
from django.contrib.auth import get_user_model

from rest_framework import permissions, status, views, serializers
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer

from knox.views import LoginView as KnoxLoginView

from .utils import create_user

User = get_user_model()


class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        return super(LoginView, self).post(request)


class CreateView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    class UserCreationSerializer(serializers.Serializer):
        email = serializers.EmailField()
        first_name = serializers.CharField()
        last_name = serializers.CharField()
        password = serializers.CharField(min_length=16)
        password_confirmation = serializers.CharField(min_length=16)

        def validate(self, data):
            """
            Check password constraints
            """

            if data["password"] != data["password_confirmation"]:
                raise serializers.ValidationError("Passwords do not match.")

            del data["password_confirmation"]

            return data

    class UserSerializer(serializers.Serializer):
        email = serializers.EmailField()
        first_name = serializers.CharField()
        last_name = serializers.CharField()

    def post(self, request):
        serializer = self.UserCreationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                user = create_user(**serializer.validated_data)
                serializer = self.UserSerializer(user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except ValueError as e:
                return Response(e.errors, status=status.HTTP_400_BAD_REQUEST)
