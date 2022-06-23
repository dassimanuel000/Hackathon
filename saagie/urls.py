"""saagie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views

urlpatterns = [
    #path('', include('hackathon.urls')),
    #path('audit/', include('hackathon.urls')),
    path('audit/', views.audit, name="audit"),
    path('hackathon/', include('hackathon.urls')),
    path('admin/', admin.site.urls),
    path('restor/', views.restore, name='restore'),
    path('copy/', views.copy, name="copy"),
]
