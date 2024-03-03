from rest_framework.viewsets import ViewSet
from rest_framework.exceptions import NotFound, PermissionDenied, ValidationError
from rest_framework.response import Response

from .models import Transaction
from .serializers import TransactionCreateSerializer, TransactionDetailSerializer


class TransactionViewSet(ViewSet):
    lookup_value_regex = "\d+"

    def list(self, request):
        pass

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
