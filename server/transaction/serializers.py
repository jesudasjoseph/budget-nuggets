from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model

from budget.models import Budget
from period.models import Period, PeriodCategory

from period.serializers import PeriodCategoryDetailSerializer

from .models import Transaction

User = get_user_model()


class TransactionPeriodCategorySerializer(serializers.Serializer):
    period_category = serializers.PrimaryKeyRelatedField(
        queryset=PeriodCategory.objects.all()
    )
    value = serializers.DecimalField(max_digits=12, decimal_places=2)


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
    period_categories = TransactionPeriodCategorySerializer(
        many=True, read_only=False, required=False
    )

    def validate(self, data):
        # Validate period
        if data["period"].budget != data["budget"]:
            raise ValidationError("Provided period must be a child of budget")

        # Validate period_categories
        if "period_categories" in data:
            total_value = 0
            for item in data["period_categories"]:
                if item["period_category"].period.budget != data["budget"]:
                    raise ValidationError(
                        "You must provide period categories that are children of this budget."
                    )
                total_value += item["value"]

            if total_value != data["value"]:
                raise ValidationError(
                    "All period_category values must add up to the transaction value."
                )

        return data
