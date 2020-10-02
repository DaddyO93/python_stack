from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.
def index (request):
    context = {
        "all_books":Book.objects.all(),
        "all_authors":Author.objects.all()
    }
    return render(request, 'index.html', context)

def display_books (request):
    return render('/')

def display_authors (request):
    return render ('/')

def display_publishers (request):
    return render ('/')
