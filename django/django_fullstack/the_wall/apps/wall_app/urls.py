from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index),
    path('home/submit_message', views.submit_message),
    path('home/submit_comment/<int:id>', views.submit_comment),
]