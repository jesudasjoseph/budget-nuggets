from django.urls import path, include
from user import urls as user_urls
from budget import urls as budget_urls

urlpatterns = [
    path(
        "api/",
        include(
            [
                path("", include(user_urls)),
                path("", include(budget_urls)),
            ]
        ),
    ),
]
