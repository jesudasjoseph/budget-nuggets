from rest_framework import serializers

from .models import Period


class PeriodDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = "__all__"


class PeriodCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ["start_date", "end_date", "budget"]


class PeriodUpdateSerializer(serializers.Serializer):
    start_date = serializers.DateField(required=False)
    end_date = serializers.DateField(required=False)
