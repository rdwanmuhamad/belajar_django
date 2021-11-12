from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('berita/', views.index),
    path('olahraga/', views.index),
]
