from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register(r"periods", views.PeriodViewSet, "period")

urlpatterns = router.urls
