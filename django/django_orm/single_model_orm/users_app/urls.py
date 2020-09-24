from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('process_info', views.process_info)
]