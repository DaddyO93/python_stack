from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('generator', views.generator),
    path('reset', views.reset),
]