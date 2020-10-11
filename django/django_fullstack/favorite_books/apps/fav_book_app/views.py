from django.shortcuts import render, redirect
from .models import Book
from apps.login_registration_app.models import User
from django.contrib import messages

# Create your views here.
def index (request):
    if 'user_id' not in request.session:
        messages.error(request, "You need to register or log in!")
        return redirect ('/')
    else:
        context = {
            "user":User.objects.get(id=request.session['user_id']),
            "all_books":Book.objects.all()
        }
    return render (request, 'books.html', context)

def add_book (request):
    if 'user_id' not in request.session:
        messages.error(request, "You need to register or log in!")
        return redirect ('/')
    else:
        if request.method == 'POST':
            errors = Book.objects.bookValidator(request.POST) 
            if len(errors)>0:
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect ('/books/home')
            user = User.objects.get(id=request.session['user_id'])         
            new_book = Book.objects.create(title=request.POST['title'], uploaded_by=user, desc=request.POST['desc'])
            new_book.users_who_like.add(user)
            return redirect ('/books/home')
        return redirect ('/books/home')

def add_to_favorites (request, id):
    if 'user_id' not in request.session:
        messages.error(request, "You need to register or log in!")
        return redirect ('/')
    else:
        if request.method == "POST":
            user = User.objects.get(id=request.session['user_id'])
            book = Book.objects.get(id=id)
            book.users_who_like.add(user)
            return redirect (f'/books/home/{id}')
        return redirect (f'/books/home/{id}')

def un_favorite (request, id):
    if 'user_id' not in request.session:
        messages.error(request, "You need to register or log in!")
        return redirect ('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        book = Book.objects.get(id=id)
        user.liked_books.remove(book)
        return redirect (f'/books/home/{id}')
            
def book_details (request, id):
    if 'user_id' not in request.session:
        messages.error(request, "You need to register or log in!")
        return redirect ('/')
    else:
        book = Book.objects.get(id=id)
        user = User.objects.get(id=request.session['user_id'])
        context = {
            "book":book,
            "user":user
        }
    return render (request, 'info.html', context)

def update_book (request, id):
    if 'user_id' not in request.session:
        messages.error(request, "You need to register or log in!")
        return redirect ('/')
    else:
        if request.method == 'POST':
            book = Book.objects.get(id=id)
            book.title = request.POST['title']
            book.desc = request.POST['desc']
            errors = Book.objects.bookValidator(request.POST) 
            if len(errors)>0:
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect ('/books/home')
            else:
                book.save()
        return redirect ('/books/home')

def delete_book (request, id):
    if 'user_id' not in request.session:
        messages.error(request, "You need to register or log in!")
        return redirect ('/')
    else:
        if request.method == "POST":
            book = Book.objects.get(id=id)
            book.delete()
            return redirect ('/books/home')
        return redirect ('/books/home')
                        
def user_books (request):
    if 'user_id' not in request.session:
        messages.error(request, "You need to register or log in!")
        return redirect ('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        context = {
            "liked_books":user.liked_books.all(),
            "uploaded_books":user.books_uploaded.all(),
            "user":user
        }
        return render (request, "liked_books.html", context)