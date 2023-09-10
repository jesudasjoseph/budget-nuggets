from django.contrib.auth import login
from django.contrib.auth.models import User

from rest_framework import permissions, viewsets
from rest_framework.authtoken.serializers import AuthTokenSerializer

from knox import views


# Create your views here.
class LoginView(views.LoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)

        return_object = super(LoginView, self).post(request, format=None)

        # try:
        #     accounts = User.objects.get(username=user).account
        #     accounts = UserAccountSerializer(data=accounts).data()
        # except User.DoesNotExist:
        #     accounts = []
        # finally:
        #     return_object.data["accounts"] = accounts
        return return_object


class AuthViewSet(viewsets.ViewSet):
    def get_permissions(self):
        if self.action == "create":
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request):
        print(request.data)
        return Response(status=status.HTTP_201_CREATED)
