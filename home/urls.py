from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    # path('student/', StudentAPIView.as_view()),
    # path('category/', CategoryAPIView.as_view()),
    # path('book/', BookAPIView.as_view()),
    # path('register/', RegisterUserAPIView.as_view()),
    #student generics
    path('student/', StudentGenericsGP.as_view()),
    path('student/<id>/', StudentGenericsUD.as_view()),
    path('category/', CategoryGenericsGP.as_view()),
    path('category/<id>/', CategoryGenericsUD.as_view()),
    path('book/', BookGenericsGP.as_view()),
    path('book/<id>/', BookGenericsUD.as_view()),
]
