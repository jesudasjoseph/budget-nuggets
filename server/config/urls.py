from django.urls import path, include
from user import urls as user_urls
from budget import urls as budget_urls
from period import urls as period_urls
from category import urls as category_urls
from transaction import urls as transaction_urls

urlpatterns = [
    path(
        "api/",
        include(
            [
                path("", include(user_urls)),
                path("", include(budget_urls)),
                path("", include(period_urls)),
                path("", include(category_urls)),
                path("", include(transaction_urls)),
            ]
        ),
    ),
]
