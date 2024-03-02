from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register(r"periods", views.PeriodViewSet, "period")
router.register(
    r"periods/(?P<period_id>[^/.]+)/categories",
    views.PeriodCategoryViewSet,
    basename="period-catgory",
)

urlpatterns = router.urls
