from datetime import date
from calendar import monthrange

from rest_framework.viewsets import ViewSet
from rest_framework.exceptions import NotFound, PermissionDenied, ValidationError
from rest_framework.response import Response

from budget.models import Budget
from category.models import Category

from .models import Period, PeriodCategory
from .serializers import (
    PeriodDetailSerializer,
    PeriodCreateSerializer,
    PeriodUpdateSerializer,
    PeriodCategorySerializer,
)


class PeriodViewSet(ViewSet):
    def list(self, request):
        if not request.query_params["budget"]:
            raise ValidationError("No budget search parameter provided")

        period_qs = Period.objects.filter(budget=request.query_params["budget"])

        if request.query_params["date"]:
            requested_date = date.fromisoformat(request.query_params["date"])
            period_qs.filter(
                start_date__gte=requested_date, end_date__lte=requested_date
            )

        serializer = PeriodDetailSerializer(period_qs, many=True)
        return Response(serializer.data, status=200)

    def create(self, request):
        serializer = PeriodCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        budget = serializer.validated_data["budget"]

        if budget.owner != request.user:
            raise PermissionDenied()

        requested_date = serializer.validated_data["date"]

        def last_day_of_month(year: int, month: int):
            return monthrange(year, month)[1]

        start_date = date.today()
        end_date = date.today()
        if budget.type == Budget.MONTHLY:
            start_date = date(requested_date.year, requested_date.month, 1)
            end_date = date(
                requested_date.year,
                requested_date.month,
                last_day_of_month(requested_date.year, requested_date.month),
            )
        elif budget.type == Budget.ANNUAL:
            start_date = date(requested_date.year, 1, 1)
            end_date = date(
                requested_date.year, 12, last_day_of_month(requested_date.year, 12)
            )

        period = Period(start_date=start_date, end_date=end_date, budget=budget)
        period.save()

        return Response(PeriodDetailSerializer(period).data, status=201)

    def retrieve(self, request, pk=None):
        try:
            period = Period.objects.get(pk=pk)
        except Period.DoesNotExist:
            raise NotFound()

        if period.budget.owner != request.user:
            raise PermissionDenied()

        serializer = PeriodDetailSerializer(period)
        return Response(serializer.data)

    def partial_update(Self, request, pk=None):
        serializer = PeriodUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        period = Period.objects.filter(pk=pk)

        if not period.exists():
            raise NotFound()

        if period[0].budget.owner != request.user:
            raise PermissionDenied()

        period.update(**serializer.validated_data)

        return Response(PeriodDetailSerializer(period[0]).data, status=200)

    def destroy(self, request, pk=None):
        try:
            period = Period.objects.get(pk=pk)
        except Period.DoesNotExist:
            raise NotFound()

        if period.budget.owner != request.user:
            raise PermissionDenied()

        period.delete()

        return Response(status=204)


class PeriodCategoryViewSet(ViewSet):
    def list(self, request, period_id):
        try:
            period = Period.objects.get(pk=period_id)
        except Period.DoesNotExist:
            raise NotFound()

        if period.budget.owner != request.user:
            raise PermissionDenied()

        period_categories = PeriodCategory.objects.filter(period=period)

        serializer = PeriodCategorySerializer(period_categories, many=True)
        return Response(serializer.data, status=200)

    def create(self, request, period_id):
        pass

    def retrieve(self, request, period_id, pk=None):
        pass

    def partial_update(self, request, period_id, pk=None):
        pass

    def destroy(self, request, period_id, pk=None):
        pass
