from rest_framework import serializers

from .models import Budget

from period.models import Period


class BudgetDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ["id", "name", "type", "owner", "users"]


class BudgetCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ["name", "type"]


class BudgetUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
