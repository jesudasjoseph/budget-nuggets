from django.urls import path, include
from . import views

urlpatterns = [
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
]
