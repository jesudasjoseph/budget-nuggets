from rest_framework import serializers

from budget.models import Budget

from .models import Period


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
