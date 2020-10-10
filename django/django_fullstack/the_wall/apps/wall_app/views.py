from django.shortcuts import render, redirect
from .models import Message, Comment
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
            "all_messages":Message.objects.all(),
            "all_comments":Comment.objects.all()
        }
    return render (request, 'wall.html', context)

def submit_message (request):
    if 'user_id' not in request.session:
        messages.error(request, "You need to register or log in!")
        return redirect ('/')
    else:
        current_user = User.objects.get(id=request.session['user_id'])
        new_message = Message.objects.create(message=request.POST['message'], commenter=current_user)
        return redirect ('/wall/home')

def submit_comment (request, id):
    if 'user_id' not in request.session:
        messages.error(request, "You need to register or log in!")
        return redirect ('/')
    else:
        one_message = Message.objects.get(id=id)
        current_user = User.objects.get(id=request.session['user_id'])
        new_comment = Comment.objects.create(comment=request.POST['comment'], parent_message=one_message, user=current_user)
        return redirect ('/wall/home')