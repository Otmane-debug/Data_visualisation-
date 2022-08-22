from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('fusion/', views.fusion, name="fusion"),
    path('ccm/', views.ccm, name="ccm"),
    path('auxiliaire/', views.auxilaire, name="auxiliaire"),
    path('fusion/graphs/', views.fusion_graphs, name="fusion_graphs"),
    path('ccm/graphs', views.ccm_graphs, name="ccm_graphs"),
    path('auxilaire/graphs', views.auxiliaire_graphs, name="auxiliaire_graphs"),
]
