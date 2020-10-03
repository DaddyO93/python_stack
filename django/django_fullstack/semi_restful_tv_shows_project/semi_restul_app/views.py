from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages
from datetime import date

# Create your views here.
def index (request):
    context = {
        "all_shows":Show.objects.all()
    }
    return render (request, 'index.html', context)

def view_show (request, id):
    context = {
            "show":Show.objects.get(id=id)
        }
    return render (request, 'shows.html', context)

def edit_show (request, id):
    context = {
        "show": Show.objects.get(id=id)
    }
    release_date = context["show"].release_date
    context["release_date"]= str(release_date)
    return render(request, 'edit.html', context)

def update_show (request, id):
    # check for errors
    errors = Show.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect (f'/shows/{id}/edit')
    if request.method=='POST':
        show_to_update = Show.objects.get(id=id)
        show_to_update.title = request.POST['title']
        show_to_update.network = request.POST['network']
        show_to_update.release_date = str(request.POST['release_date'])
        show_to_update.desc = request.POST['desc']
        show_to_update.save()
        return redirect(f'/shows/{show_to_update.id}')
        
def create_form (request):
    return render(request, 'add.html')

def add_show(request):
    if request.method=='POST':
        # check for errors
        errors = Show.objects.basic_validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect ('/shows/new')        
        new_show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], desc=request.POST['desc']) 
        new_show.save()
        return redirect(f'/shows/{new_show.id}')

def destroy_show (request, id):
    if request.method=='POST':
        show_to_delete=Show.objects.get(id=id)
        show_to_delete.delete()
    return redirect('/')
