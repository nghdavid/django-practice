"""ithome URL Configuration

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
from django.urls import path, include
from . import views
from .views import VendorListView,VendorDetailView, VendorCreateView,VendorUpdateView
app_name = 'vendors'
'''
urlpatterns = [
    # 後方的 name 可以先忽略，目前不會用到
    #path('', views.vendor_index, name="vendor_index"),
    path('', views.showtemplate,name='index'),
    path('<int:id>/', views.singleVendor, name='vendor_id'),
    path('create', views.vendor_create_view,name='create'), # 新增
]
'''
urlpatterns = [
    path('', VendorListView.as_view(), name='index'),
    path('<int:pk>/', VendorDetailView.as_view(), name='vendor_id'),
    path('create/', VendorCreateView.as_view(), name='create'),
    path('<int:pk>/update/', VendorUpdateView.as_view(), name='update'), 
]
