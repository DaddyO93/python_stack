from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index (request):
    return render(request, 'index.html')

def generator (request):
    request.session['word'] = get_random_string(length=14)
    request.session['counter'] = request.session.get('counter', 0) +1
    return redirect ("/")

def reset (request):
    request.session['counter'] = 0
    return redirect ('/')