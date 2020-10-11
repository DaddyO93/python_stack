from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index),
    path('home/add_book', views.add_book),
    path('home/add_to_favorites/<int:id>', views.add_to_favorites),
    path('home/<int:id>', views.book_details),
    path('home/update_book/<int:id>', views.update_book),
    path('home/delete_book/<int:id>', views.delete_book),
    path('home/user_books', views.user_books),
    path('home/un_favorite/<int:id>', views.un_favorite)
]