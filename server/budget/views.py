from rest_framework.viewsets import ViewSet
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.response import Response

from .models import Budget
from .serializers import (
    BudgetDetailSerializer,
    BudgetCreateSerializer,
    BudgetUpdateSerializer,
)


class BudgetViewSet(ViewSet):
    lookup_value_regex = "\d+"

    def list(self, request):
        budget_qs = Budget.objects.filter(owner=request.user)

        serializer = BudgetDetailSerializer(budget_qs, many=True)
        return Response(serializer.data, status=200)

    def create(self, request):
        serializer = BudgetCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        budget = Budget(**serializer.validated_data, owner=self.request.user)
        budget.save()

        return Response(BudgetDetailSerializer(budget).data, status=201)

    def retrieve(self, request, pk=None):
        try:
            budget = Budget.objects.get(pk=pk)
        except Budget.DoesNotExist:
            raise NotFound()

        if budget.owner != request.user:
            raise PermissionDenied()

        serializer = BudgetDetailSerializer(budget)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        serializer = BudgetUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        budget = Budget.objects.filter(pk=pk)

        if not budget.exists():
            raise NotFound()

        if budget[0].owner != request.user:
            raise PermissionDenied()

        budget.update(**serializer.validated_data)

        return Response(BudgetDetailSerializer(budget[0]).data, status=200)

    def destroy(self, request, pk=None):
        try:
            budget = Budget.objects.get(pk=pk)
        except Budget.DoesNotExist:
            raise NotFound()

        if budget.owner != request.user:
            raise PermissionDenied()

        budget.delete()

        return Response(status=204)
