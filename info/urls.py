from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='info-home'),
    path('about/', views.About, name='info-about'),
]
