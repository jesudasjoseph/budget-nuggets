from rest_framework import serializers

from .models import Budget, Period


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


class PeriodDetailSerializer(serializers.ModelSerializer):
    label = serializers.CharField()

    class Meta:
        model = Period
        fields = "__all__"


class PeriodCreateSerializer(serializers.Serializer):
    date = serializers.DateField()


class PeriodUpdateSerializer(serializers.Serializer):
    start_date = serializers.DateField(required=False)
    end_date = serializers.DateField(required=False)
