"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from rest_framework.schemas import get_schema_view # built-in support for Core API
from rest_framework.documentation import include_docs_urls # make the API humanly readabe

schema_view = get_schema_view(title='Learning Log API') # built-in support for Core API

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #incude urls from topic app
    path('api/v1/', include('topic.urls')),

    #handles CRUD permissions
    path('api-auth/', include('rest_framework.urls')),

    #Login,logout and password reset endpoints
    path('api/v1/rest-auth/', include('rest_auth.urls')),

    #registration
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),

    #built-in support for Core API
    path('schema/', schema_view),

    # make the API humanly readabe
    path('docs/', include_docs_urls(title='Learning Log API')),
]
