from rest_framework.views import APIView
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.response import Response

from budget.models import Budget

from .models import Category
from .serializers import (
    CategoryDetailSerializer,
    CategoryCreateSerializer,
    CategoryUpdateSerializer,
)


class CategoryDetailAPIView(APIView):
    def get(self, request, category_id):
        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            raise NotFound()

        if category.budget.owner != request.user:
            raise PermissionDenied()

        serializer = CategoryDetailSerializer(category)
        return Response(serializer.data)


class CategoryCreateAPIView(APIView):
    def post(self, request):
        serializer = CategoryCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        budget = serializer.validated_data["budget"]

        if budget.owner != request.user:
            raise PermissionDenied()

        category = Category(**serializer.validated_data)
        category.save()

        return Response(CategoryDetailSerializer(category).data, status=201)
