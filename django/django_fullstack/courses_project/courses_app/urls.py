from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_course', views.add_course),
    path('<int:id>', views.comment_view),
    path('<int:id>/add_comment', views.comment_add),
    path('<int:id>/destroy', views.delete_course_confirm),
    path('<int:id>/confirm_destroy', views.delete_course)
]