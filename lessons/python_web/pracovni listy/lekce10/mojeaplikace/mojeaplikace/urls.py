"""
URL configuration for mojeaplikace project.

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
from django.contrib import admin
from django.urls import path
from zamestnanci import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('zamestnanci/', views.zamestnanci_list, name='zamestnanci_list'),
    path('zamestnanci/<int:empno>/', views.zamestnanec_detail, name='zamestnanec_detail'),
    path('zamestnanci/add/', views.zamestnanec_add, name='zamestnanec_add'),
    path('zamestnanci/<int:empno>/edit/', views.zamestnanec_edit, name='zamestnanec_edit'),
    path('zamestnanci/<int:empno>/delete/', views.zamestnanec_delete, name='zamestnanec_delete'),
    path('oddeleni/', views.oddeleni_list, name='oddeleni_list'),
    path('oddeleni/<int:deptno>/', views.oddeleni_detail, name='oddeleni_detail'),
    path('oddeleni/add/', views.oddeleni_add, name='oddeleni_add'),
    path('oddeleni/<int:deptno>/edit/', views.oddeleni_edit, name='oddeleni_edit'),
    path('oddeleni/<int:deptno>/delete/', views.oddeleni_delete, name='oddeleni_delete'),
]
