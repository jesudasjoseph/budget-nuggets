from django.contrib.auth import login, authenticate
from django.contrib.auth import get_user_model

from rest_framework import permissions, status, views, serializers
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer

from knox.views import LoginView as KnoxLoginView

from .utils import create_user

User = get_user_model()


# Create your views here.
class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        return super(LoginView, self).post(request, format=None)


class CreateView(views.APIView):
    def create(self, request):
        try:
            user = create_user(**request.data)
            return Response(data=user, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response(data=e.errors, status=status.HTTP_400_BAD_REQUEST)
