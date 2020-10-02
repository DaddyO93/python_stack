from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('shows/new', views.create_form),
    path('shows/add', views.add_show),
    path('shows/<int:id>', views.view_show),
    path('shows/<int:id>/edit', views.edit_show),
    path('shows/<int:id>/destroy', views.destroy_show)
    ]