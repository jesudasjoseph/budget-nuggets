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

        if serializer.validated_data["budget"].owner != request.user:
            raise PermissionDenied()

        period = Period(**serializer.validated_data)
        period.save()

        return Response(PeriodDetailSerializer(period).data, status=201)


class PeriodUpdateAPIView(APIView):
    def patch(self, request, period_id):
        serializer = PeriodUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            period = Period.objects.get(pk=period_id)
        except Period.DoesNotExist:
            raise NotFound()

        if period.budget.owner != request.user:
            raise PermissionDenied()

        period.start_date = serializer.validated_data["start_date"]
        period.end_date = serializer.validated_data["end_date"]
        period.save()

        return Response(PeriodDetailSerializer(period).data, status=200)
