from rest_framework import serializers

from period.models import Period

from .models import Category


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CategoryCreateSerializer(serializers.ModelSerializer):
    color = serializers.CharField(max_length=7, allow_blank=True, required=False)

    class Meta:
        model = Category
        fields = "__all__"


class CategoryUpdateSerializer(serializers.Serializer):
    label = serializers.CharField(required=False)
    color = serializers.CharField(max_length=7, required=False)
