from rest_framework import serializers
from django.contrib.auth import get_user_model

from budget.models import Budget
from period.models import Period

from period.serializers import PeriodCategoryDetailSerializer

from .models import Transaction

User = get_user_model()


class TransactionParamSerializer(serializers.Serializer):
    budget = serializers.PrimaryKeyRelatedField(queryset=Budget.objects.all())
    period = serializers.PrimaryKeyRelatedField(
        queryset=Period.objects.all(), required=False
    )
    from_date = serializers.DateField(required=False)
    to_date = serializers.DateField(required=False)


class TransactionDetailSerializer(serializers.ModelSerializer):
    period_categories = PeriodCategoryDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Transaction
        fields = "__all__"


class TransactionCreateSerializer(serializers.Serializer):
    value = serializers.DecimalField(max_digits=12, decimal_places=2)
    merchant = serializers.CharField(required=False)
    notes = serializers.CharField(required=False)
    date = serializers.DateField(required=False)
    budget = serializers.PrimaryKeyRelatedField(queryset=Budget.objects.all())
    period = serializers.PrimaryKeyRelatedField(queryset=Period.objects.all())
