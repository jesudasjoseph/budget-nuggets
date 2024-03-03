from datetime import date

from rest_framework.viewsets import ViewSet
from rest_framework.exceptions import NotFound, PermissionDenied, ValidationError
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Period, PeriodCategory
from .serializers import (
    PeriodDetailSerializer,
    PeriodCreateSerializer,
    PeriodCreateNextSerializer,
    PeriodUpdateSerializer,
    PeriodCategoryDetailSerializer,
    PeriodCategoryCreateSerializer,
    PeriodCategoryUpdateSerializer,
)
from .utils import get_next_date_range, get_date_range_from_date


class PeriodViewSet(ViewSet):
    lookup_value_regex = "\d+"

    def list(self, request):
        if not request.query_params["budget"]:
            raise ValidationError("No budget search parameter provided")

        period_qs = Period.objects.filter(budget=request.query_params["budget"])

        if "date" in request.query_params:
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

        start_date, end_date = get_date_range_from_date(
            requested_date=requested_date, period_type=budget.type
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

    @action(methods=["post"], detail=False)
    def create_next(self, request):
        serializer = PeriodCreateNextSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        budget = serializer.validated_data["budget"]

        if budget.owner != request.user:
            raise PermissionDenied()

        period = serializer.validated_data["period"]

        start_date, end_date = get_next_date_range(period.end_date, budget.type)

        period = Period(start_date=start_date, end_date=end_date, budget=budget)
        period.save()

        return Response(PeriodDetailSerializer(period).data, status=201)


class PeriodCategoryViewSet(ViewSet):
    lookup_value_regex = "\d+"

    def list(self, request, period_id):
        try:
            period = Period.objects.get(pk=period_id)
        except Period.DoesNotExist:
            raise ValidationError()

        if period.budget.owner != request.user:
            raise PermissionDenied()

        period_categories = PeriodCategory.objects.filter(period=period)

        serializer = PeriodCategoryDetailSerializer(period_categories, many=True)
        return Response(serializer.data, status=200)

    def create(self, request, period_id):
        serializer = PeriodCategoryCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            period = Period.objects.get(pk=period_id)
        except Period.DoesNotExist:
            raise ValidationError()

        if period.budget.owner != request.user:
            raise PermissionDenied()

        period_category = PeriodCategory.objects.create(**serializer.validated_data)

        return Response(
            PeriodCategoryDetailSerializer(period_category).data, status=201
        )

    def retrieve(self, request, period_id, pk=None):
        try:
            period = Period.objects.get(pk=period_id)
        except Period.DoesNotExist:
            raise ValidationError()

        if period.budget.owner != request.user:
            raise PermissionDenied()

        try:
            period_category = PeriodCategory.objects.get(pk=pk)
        except PeriodCategory.DoesNotExist:
            raise NotFound()

        return Response(PeriodCategoryDetailSerializer(period_category).data)

    def partial_update(self, request, period_id, pk=None):
        serializer = PeriodCategoryUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            period = Period.objects.get(pk=period_id)
        except Period.DoesNotExist:
            raise ValidationError()

        if period.budget.owner != request.user:
            raise PermissionDenied()

        period_category_qs = PeriodCategory.objects.filter(pk=pk)

        if not period_category_qs.exists():
            raise NotFound()

        period_category_qs.update(**serializer.validated_data)

        return Response(
            PeriodCategoryDetailSerializer(period_category_qs[0]).data, status=204
        )

    def destroy(self, request, period_id, pk=None):
        try:
            period = Period.objects.get(pk=period_id)
        except Period.DoesNotExist:
            raise ValidationError()

        if period.budget.owner != request.user:
            raise PermissionDenied()

        try:
            period_category = PeriodCategory.objects.get(pk=pk)
        except PeriodCategory.DoesNotExist:
            raise NotFound()

        period_category.delete()

        return Response(status=204)
