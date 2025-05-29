"""
URL configuration for ronoos_cake project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.http import HttpResponse
from django.shortcuts import redirect

def home(request):
    return HttpResponse("Welcome to the homepage!")

def root_redirect(request):
    return redirect('/api/v1/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('backend.apps.cakes.api.urls')),
    path('api/v1/', include('backend.apps.users.api.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('home/', home, name='home'),
    path('', home, name='home'),
    path('', root_redirect),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
