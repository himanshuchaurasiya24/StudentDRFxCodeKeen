from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('student/', StudentAPIView.as_view()),
    path('category/', CategoryAPIView.as_view()),
    path('book/', BookAPIView.as_view()),
    path('register/', RegisterUserAPIView.as_view()),
]
