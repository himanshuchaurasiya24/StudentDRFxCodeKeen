from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', home),
    path('post/', post_student),
    path('update/', update_student),
    path('partial-update/', partial_update_student),
    path('delete/', delete_student),
]
