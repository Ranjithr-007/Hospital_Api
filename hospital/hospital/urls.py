"""hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, re_path, include
from users import views
from users.views import *
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from rest_framework.schemas.openapi import SchemaGenerator

schema_view = get_schema_view(
    title='Server Monitoring API',
    url='https://www.example.org/api/'
)

schema_view = get_schema_view(
    title='Server Monitoring API',
    url='https://www.example.org/api/',
    urlconf='hospital.urls',
)


urlpatterns = [
    path('api/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
    path('redoc/', TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='redoc'),
    path('openapi', get_schema_view(
        title="API",
        description="API for all things …",
        version=""
    ), name='openapi-schema'),
    path('admin/', admin.site.urls),
    
    path('api/register/',views.RegisterUser.as_view(),name="register_user"),
    path('api/login/',obtain_auth_token,name="login"),
    path('api/welcome/',views.welcome.as_view(),name="welcome"),
    # path('api/userDetails/<int:pk>/',views.userDetails.as_view(),name="userDetails"),
    # path('api/paginationApi/',views.paginationApi.as_view(),name="paginationApi"),
    
    
]
