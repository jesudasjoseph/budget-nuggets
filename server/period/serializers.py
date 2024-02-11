from rest_framework import serializers

from budget.models import Budget
from category.serializers import CategoryDetailSerializer

from .models import Period, PeriodCategory


class PeriodDetailSerializer(serializers.ModelSerializer):
    label = serializers.CharField()

    class Meta:
        model = Period
        fields = "__all__"


class PeriodCreateSerializer(serializers.Serializer):
    date = serializers.DateField()
    budget = serializers.PrimaryKeyRelatedField(queryset=Budget.objects.all())


class PeriodUpdateSerializer(serializers.Serializer):
    start_date = serializers.DateField(required=False)
    end_date = serializers.DateField(required=False)


class PeriodCategoryDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    category = CategoryDetailSerializer()
    value = serializers.DecimalField(max_digits=12, decimal_places=2)


class PeriodCategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodCategory
        fields = "__all__"


class PeriodCategoryUpdateSerializer(serializers.Serializer):
    value = serializers.DecimalField(max_digits=12, decimal_places=2)
