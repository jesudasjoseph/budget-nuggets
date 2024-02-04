from rest_framework import serializers

from ..models import Period


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
