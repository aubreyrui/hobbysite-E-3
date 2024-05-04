"""
URL configuration for hobbysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace = 'blog')),
    path('', include('wiki.urls', namespace = 'wiki')),
    path('', include('commissions.urls', namespace='commissions')),
<<<<<<< HEAD
    path('merchstore/', include('merchstore.urls', namespace='merchstore')),
=======
    path('merch/', include('merchstore.urls', namespace='merchstore')),
>>>>>>> 94c71c04d2f3762380d36f8551728a3504fe181e
    path('',include('user_management.urls', namespace ="user_management"))
]
