from rest_framework.viewsets import ViewSet
from rest_framework.exceptions import NotFound, PermissionDenied, ValidationError
from rest_framework.response import Response

from .models import Transaction
from .serializers import (
    TransactionCreateSerializer,
    TransactionDetailSerializer,
    TransactionParamSerializer,
)


class TransactionViewSet(ViewSet):
    lookup_value_regex = "\d+"

    def list(self, request):
        param_serializer = TransactionParamSerializer(data=request.query_params)
        param_serializer.is_valid(raise_exception=True)

        params = param_serializer.validated_data

        budget = params["budget"]

        if not budget:
            raise ValidationError("Please provide a 'budget' parameter.")

        if budget.owner != request.user:
            raise PermissionDenied()

        transaction_qs = Transaction.objects.filter(budget=budget)

        if "period" in params:
            if params["period"].budget != budget:
                raise PermissionDenied()
            transaction_qs = transaction_qs.filter(period=params["period"])

        if "from_date" in params:
            transaction_qs = transaction_qs.filter(date__gte=params["from_date"])

        if "to_date" in params:
            transaction_qs = transaction_qs.filter(date__lte=params["to_date"])

        return Response(
            TransactionDetailSerializer(
                transaction_qs.order_by("date"), many=True
            ).data,
            status=200,
        )

    def create(self, request):
        serializer = TransactionCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        budget = serializer.validated_data["budget"]
        period = serializer.validated_data["period"]

        if budget.owner != request.user:
            raise PermissionDenied()

        if period.budget != budget:
            raise ValidationError()

        transaction = Transaction(**serializer.validated_data, user=request.user)
        transaction.save()

        return Response(TransactionDetailSerializer(transaction).data, status=201)

    def retrieve(self, request, pk=None):
        return Response(status=501)

    def partial_update(self, request, pk=None):
        return Response(status=501)

    def destroy(self, request, pk=None):
        try:
            transaction = Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            raise NotFound()

        if transaction.budget.owner != request.user:
            raise PermissionDenied()

        transaction.delete()
        return Response(status=204)
