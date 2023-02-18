from django.shortcuts import render
from knox import views
from rest_framework.authentication import BasicAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class LoginView(views.LoginView):
    authentication_classes = [BasicAuthentication]
