from rest_framework import serializers
from accounts.models import Account


class AccountSerializer(serializers.Serializer):
    class Meta:
        modal = Account
        fields = ["id", "account_name", "created"]
