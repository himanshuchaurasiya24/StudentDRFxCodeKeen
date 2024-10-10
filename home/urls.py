from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', home),
    path('post-student/', post_student),
    path('update-student/', update_student),
    path('pupdate-student/', partial_update_student),
    path('delete-student/', delete_student),
    path('book/', get_book),
    path('post-book/', post_book),
    path('update-book/', update_book),
    path('patch-book/', patch_book),
    path('delete-book/', delete_book),
    path('category/', get_category),
    path('post-category/', post_category),
    path('update-category/', update_category),
    path('patch-category/', patch_category),
    path('delete-category/', delete_category)

]
