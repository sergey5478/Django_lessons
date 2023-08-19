from django.urls import path
from . import views

urlpatterns = [
    path('coin/', views.coin, name='coin'),
    path('cube/', views.cube, name='cube'),
    path('rand100/', views.rand100, name='rand100'),
    path('main_hw/', views.main_hw, name='main_hw'),
    path('about_me/', views.about_me, name='about_me'),
]
