from django.urls import path, include
from knox.views import LogoutView, LogoutAllView
from . import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name='knox_login'),
    path("logout/", LogoutView.as_view(), name="knox_logout"),
    path("lohoutall/", LogoutAllView.as_view(), name="knox_logout_all")
]