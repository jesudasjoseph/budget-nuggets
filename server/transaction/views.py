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

        budget = param_serializer.validated_data["budget"]
        period = param_serializer.validated_data["period"]
        from_date = param_serializer.validated_data["from_date"]
        to_date = param_serializer.validated_data["to_date"]

        if not (period or from_date or to_date):
            raise ValidationError(
                "Please provide atleast one of the following query parameters: 'period', 'from_date' or, 'to_date'"
            )

        if not budget:
            raise ValidationError("Please provide a 'budget' parameter.")
        elif budget.owner != request.user:
            raise PermissionDenied()

        transaction_qs = Transaction.objects.filter(budget=budget)

        if period:
            transaction_qs = transaction_qs.filter(period=period)

        if from_date:
            transaction_qs = transaction_qs.filter(date__gte=from_date)

        if to_date:
            transaction_qs = transaction_qs.filter(date__lte=to_date)

        return Response(
            TransactionDetailSerializer(transaction_qs, many=True).data, status=200
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
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        try:
            transaction = Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            raise NotFound()

        if transaction.budget.owner != request.user:
            raise PermissionDenied()

        transaction.delete()
        return Response(status=204)
