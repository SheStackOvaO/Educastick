"""educastick URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from teachersPage import views

from educastick import settings

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('tests/', views.tests, name='tests'),
    path('answers/', views.answers, name='answers'),
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('account/', views.account, name='account'),
    path('test/', views.test),
    path('statistics/', views.statistics, name='statistics'),
    path('statistic/', views.calcStatistic, name='statistic'),
    path('add/', views.TypeGroupCreateView.as_view(), name='add'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
