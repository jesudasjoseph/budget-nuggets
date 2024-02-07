from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register(r"budgets", views.BudgetViewSet, "budget")

urlpatterns = router.urls
