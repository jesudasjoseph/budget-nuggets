from django.urls import include, path
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register(r"periods", views.PeriodViewSet, "period")

category_router = SimpleRouter()
category_router.register(r"categories", views.PeriodCategoryViewSet, "period-category")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "periods/<int:period_id>/categories/",
        views.PeriodCategoryViewSet.as_view({"get": "list"}),
    ),
]
