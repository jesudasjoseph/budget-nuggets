from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.serializers import AuthTokenSerializer
from accounts.models import Account
from user.models import Accounts, User
from accounts.serializers import AccountSerializer


# Create your views here.
class AccountViewSet(viewsets.ViewSet):
    def list(self, request):
        user = User.objects.get(user=request.user)
        print(user)
        account_ids = Accounts.objects.filter(user=user)
        print(account_ids)

        queryset = Account.objects.filter(id_in=account_ids)
        serializer = AccountSerializer(queryset, many=True)

        if not serializer.data:
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.data)
