from rest_framework.views import APIView
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.response import Response

from budget.models import Budget

from ..models import Category
from ..serializers import (
    CategoryDetailSerializer,
    CategoryCreateSerializer,
    CategoryUpdateSerializer,
)


class CategoryDetailAPIView(APIView):
    def get(self, request, budget_id, period_id, category_id):
        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            raise NotFound()

        if category.period.budget.owner != request.user:
            raise PermissionDenied()

        serializer = CategoryDetailSerializer(category)
        return Response(serializer.data)
