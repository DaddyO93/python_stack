from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('other_page', views.other_page)
]