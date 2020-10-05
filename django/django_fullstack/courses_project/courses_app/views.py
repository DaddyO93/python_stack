from django.shortcuts import render, redirect
from .models import Course, Description, Comment
from django.contrib import messages

# Create your views here.
def index (request):
    context = {
        'all_courses':Course.objects.all()
    }
    return render(request, 'index.html', context)

def add_course (request):
    if request.method == 'POST':
        print(request.POST['desc'])
        errors = Course.objects.basic_validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect ('/')
        else:
            new_course = Course.objects.create(name=request.POST['name'])
            new_desc = Description.objects.create(desc=request.POST['desc'], course_name=new_course)
            new_course.save()
            return redirect('/')

def comment_view (request, id):
    course = Course.objects.get(id=id)
    context = {
        'all_comments':course.comment.all(),
        'course':course
    }
    return render (request, 'comments.html', context)

def comment_add (request, id):
    course = Course.objects.get(id=id)
    if request.method == 'POST':
        new_comment = Comment.objects.create(comment=request.POST['new_comment'], course_name=course)
        new_comment.save()
        return redirect(f'/{id}')

def delete_course_confirm (request, id):
    context = {
        'course':Course.objects.get(id=id)
    }
    return render (request, 'destroy.html', context)

def delete_course (request, id):
    if request.method == 'POST':
        course_to_delete = Course.objects.get(id=id)
        course_to_delete.delete()
        return redirect ('/')