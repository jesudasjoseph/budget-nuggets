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


class PeriodUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ["start_date", "end_date"]
