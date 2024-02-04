from django.urls import path, include
from . import views

urlpatterns = [
    path(
        "category/",
        include(
            [
                path(
                    "<int:category_id>/",
                    include(
                        [
                            path(
                                "",
                                view=views.CategoryDetailAPIView.as_view(),
                            ),
                        ]
                    ),
                )
            ]
        ),
    )
]
