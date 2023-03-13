from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.serializers import AuthTokenSerializer
from accounts.models import Account


# Create your views here.
class AccountViewSet(viewsets.ViewSet):
    def list(self, request):
        # queryset = Account.objects.filter(user=request.user)
        print(request.user)
        print("list")
        return Response({"accounts": "None"})
