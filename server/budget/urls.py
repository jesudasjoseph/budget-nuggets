from django.urls import path, include
from . import views

urlpatterns = [
    path(
        "budget/",
        include(
            [
                path("", view=views.BudgetListAPIView.as_view()),
                path("create/", view=views.BudgetCreateAPIView.as_view()),
                path(
                    "<int:budget_id>/",
                    include(
                        [
                            path("", view=views.BudgetDetailAPIView.as_view()),
                            path("delete/", view=views.BudgetDeleteAPIView.as_view()),
                            path("update/", view=views.BudgetUpdateAPIView.as_view()),
                        ]
                    ),
                ),
            ]
        ),
    ),
]
