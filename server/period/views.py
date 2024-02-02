from datetime import date
from calendar import monthrange

from rest_framework.views import APIView
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.response import Response

from budget.models import Budget

from .models import Period
from .serializers import (
    PeriodDetailSerializer,
    PeriodCreateSerializer,
    PeriodUpdateSerializer,
)


class PeriodDetailAPIView(APIView):
    def get(self, request, period_id):
        try:
            period = Period.objects.get(pk=period_id)
        except Period.DoesNotExist:
            raise NotFound()

        if period.budget.owner != request.user:
            raise PermissionDenied()

        serializer = PeriodDetailSerializer(period)
        return Response(serializer.data)


class PeriodDeleteAPIView(APIView):
    def delete(self, request, period_id):
        try:
            period = Period.objects.get(pk=period_id)
        except Period.DoesNotExist:
            raise NotFound()

        if period.budget.owner != request.user:
            raise PermissionDenied()

        period.delete()

        return Response(status=204)


class PeriodCreateAPIView(APIView):
    def post(self, request):
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


class PeriodUpdateAPIView(APIView):
    def patch(self, request, period_id):
        serializer = PeriodUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        period = Period.objects.filter(pk=period_id)

        if not period.exists():
            raise NotFound()

        if period[0].budget.owner != request.user:
            raise PermissionDenied()

        period.update(**serializer.validated_data)

        return Response(PeriodDetailSerializer(period[0]).data, status=200)
