from rest_framework.views import APIView
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.response import Response

from .models import Budget
from .serializers import (
    BudgetDetailSerializer,
    BudgetCreateSerializer,
    BudgetUpdateSerializer,
)


class BudgetDetailAPIView(APIView):
    def get(self, request, budget_id):
        try:
            budget = Budget.objects.get(pk=budget_id)
        except Budget.DoesNotExist:
            raise NotFound()

        if budget.owner != request.user:
            raise PermissionDenied()

        serializer = BudgetDetailSerializer(budget)
        return Response(serializer.data)


class BudgetDeleteAPIView(APIView):
    def post(seflt, request, budget_id):
        try:
            budget = Budget.objects.get(pk=budget_id)
        except Budget.DoesNotExist:
            raise NotFound()

        if budget.owner != request.user:
            raise PermissionDenied()

        budget.delete()

        return Response(status=204)


class BudgetCreateAPIView(APIView):
    def post(self, request):
        serializer = BudgetCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        budget = Budget(**serializer.validated_data, owner=self.request.user)
        budget.save()

        return Response(BudgetDetailSerializer(budget).data, status=201)


class BudgetUpdateAPIView(APIView):
    def patch(self, request, budget_id):
        serializer = BudgetUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        budget = Budget.objects.filter(id=budget_id)

        if not budget.exists():
            raise NotFound()

        if budget[0].owner != request.user:
            raise PermissionDenied()

        budget.update(**serializer.validated_data)

        return Response(BudgetDetailSerializer(budget[0]).data, status=200)

    def put(self, request, budget_id):
        self.patch(request, budget_id)


class BudgetListAPIView(APIView):
    def get(self, request):
        budget_qs = Budget.objects.filter(owner=request.user)

        serializer = BudgetDetailSerializer(budget_qs, many=True)
        return Response(serializer.data, status=200)
