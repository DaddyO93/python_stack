from django.shortcuts import render, redirect
from .models import User, UserManager
from django.contrib import messages
import bcrypt

# Create your views here.
def index (request):
    return render (request, 'index.html')

def log_out (request):
    request.session.clear()
    return redirect ('/')

def register (request):
    if request.method =='POST':
        errors = User.objects.loginValidator(request.POST) 
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect ('/')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], b_day=request.POST['b_day'], email=request.POST['email'], password=pw_hash)
            request.session['user_id'] = new_user.id
            return redirect ("/success")
    else:
        return redirect ('/')

def login (request):
    if request.method == 'GET':
        return redirect ('/')
    if request.method == 'POST':
        user = User.objects.filter(email=request.POST['email'])
        if len(user)>0:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['user_id'] = logged_user.id
                return redirect ('/success')
            else:
                messages.error(request, "Your Email or Password are incorrect!")
                return redirect ('/')
        else:
            messages.error(request, "You must register first!")
            return redirect ('/')
    
def success_screen (request):
    if 'user_id' not in request.session:
        messages.error(request, "You need to register or log in!")
        return redirect ('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user':user
    }
    return redirect ('books/home', context)