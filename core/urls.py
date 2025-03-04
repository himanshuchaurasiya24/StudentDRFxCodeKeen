"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
    
urlpatterns = [
    path('', include('home.urls')),
    path('book/', include('home.urls')),
    path('admin/', admin.site.urls),
    
    # for session authentication
    # path('api-token-auth/', views.obtain_auth_token)
    # for jwt authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token-obtain-pair-view'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token-obtain-refresh-view')
    ]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns+=staticfiles_urlpatterns()

