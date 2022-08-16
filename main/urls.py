from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('fusion/', views.fusion, name="fusion"),
    path('ccm/', views.ccm, name="ccm"),
]
