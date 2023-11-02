from django.urls import path, include
from knox.views import LogoutView, LogoutAllView
from . import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="knox_login"),
    path("logout/", LogoutView.as_view(), name="knox_logout"),
    path("logoutall/", LogoutAllView.as_view(), name="knox_logout_all"),
    path("create/", views.AuthViewSet.as_view({"post": "create"})),
]
