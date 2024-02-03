from django.urls import path, include
from . import views

period_urls = (
    path(
        "period/",
        include(
            [
                path(
                    "create/",
                    view=views.PeriodCreateAPIView.as_view(),
                ),
                path("", view=views.PeriodListAPIView.as_view()),
                path(
                    "<int:period_id>/",
                    include(
                        [
                            path(
                                "",
                                view=views.PeriodDetailAPIView.as_view(),
                            ),
                            path(
                                "delete/",
                                view=views.PeriodDeleteAPIView.as_view(),
                            ),
                            path(
                                "update/",
                                view=views.PeriodUpdateAPIView.as_view(),
                            ),
                        ]
                    ),
                ),
            ]
        ),
    ),
)

urlpatterns = [
    path(
        "budget/",
        include(
            [
                path("", view=views.budget.BudgetListAPIView.as_view()),
                path("create/", view=views.budget.BudgetCreateAPIView.as_view()),
                path(
                    "<int:budget_id>/",
                    include(
                        [
                            path("", view=views.budget.BudgetDetailAPIView.as_view()),
                            path(
                                "delete/",
                                view=views.budget.BudgetDeleteAPIView.as_view(),
                            ),
                            path(
                                "update/",
                                view=views.budget.BudgetUpdateAPIView.as_view(),
                            ),
                            path(
                                "period/",
                                include(
                                    [
                                        path(
                                            "create/",
                                            view=views.PeriodCreateAPIView.as_view(),
                                        ),
                                        path(
                                            "", view=views.PeriodListAPIView.as_view()
                                        ),
                                        path(
                                            "<int:period_id>/",
                                            include(
                                                [
                                                    path(
                                                        "",
                                                        view=views.PeriodDetailAPIView.as_view(),
                                                    ),
                                                    path(
                                                        "delete/",
                                                        view=views.PeriodDeleteAPIView.as_view(),
                                                    ),
                                                    path(
                                                        "update/",
                                                        view=views.PeriodUpdateAPIView.as_view(),
                                                    ),
                                                ]
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                        ]
                    ),
                ),
            ]
        ),
    ),
]
