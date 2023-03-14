from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import permissions


# Create your views here.
class UserViewSet(viewsets.ViewSet):
    def get_permissions(self):
        if self.action == "create":
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request):
        print(request.data)
        return Response(status=status.HTTP_201_CREATED)
