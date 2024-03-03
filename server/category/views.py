from rest_framework.viewsets import ViewSet
from rest_framework.exceptions import NotFound, PermissionDenied, ValidationError
from rest_framework.response import Response

from .models import Category
from .serializers import (
    CategoryDetailSerializer,
    CategoryCreateSerializer,
    CategoryUpdateSerializer,
)


class CategoryViewSet(ViewSet):
    lookup_value_regex = "\d+"

    def list(self, request):
        if not request.query_params["budget"]:
            raise ValidationError("No budget search parameter provided")

        category_qs = Category.objects.filter(budget=request.query_params["budget"])

        serializer = CategoryDetailSerializer(category_qs, many=True)
        return Response(serializer.data, status=200)

    def create(self, request):
        serializer = CategoryCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        budget = serializer.validated_data["budget"]

        if budget.owner != request.user:
            raise PermissionDenied()

        category = Category(**serializer.validated_data)
        category.save()

        return Response(CategoryDetailSerializer(category).data, status=201)

    def retrieve(self, request, pk=None):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise NotFound()

        if category.budget.owner != request.user:
            raise PermissionDenied()

        serializer = CategoryDetailSerializer(category)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        serializer = CategoryUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        category_qs = Category.objects.filter(pk=pk)

        if not category_qs.exists():
            raise NotFound()

        if category_qs[0].budget.owner != request.user:
            raise PermissionDenied()

        category_qs.update(**serializer.validated_data)

        return Response(CategoryDetailSerializer(category_qs[0]).data, status=200)

    def destroy(self, request, pk=None):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise NotFound()

        if category.budget.owner != request.user:
            raise PermissionDenied()

        category.delete()

        return Response(status=204)
