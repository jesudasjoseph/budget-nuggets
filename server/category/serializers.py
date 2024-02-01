from rest_framework import serializers

from .models import Category


class CategoryDetailSerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = "__all__"
