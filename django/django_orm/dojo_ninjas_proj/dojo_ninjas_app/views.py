from django.shortcuts import render, redirect
from .models import Dojo, Ninja

# Create your views here.
def index (request):
    context = {
        "all_dojos":Dojo.objects.all(),
        "all_ninjas":Ninja.objects.all()
    }

    return render (request, 'index.html', context)

def add_dojo (request):
    Dojo.objects.create(name=request.POST['name'], city=request.POST['city'], state=request.POST['state'])
    return redirect('/')

def add_ninja (request):
    dojo = Dojo.objects.get(id=request.POST['dojo'])
    Ninja.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], dojo=dojo)
    return redirect('/')

def delete_dojo (request):
    dojo = Dojo.objects.get(name=request.POST['name'])
    dojo.delete()
    return redirect('/')

def delete_ninja (request):
    ninja = Ninja.objects.get(first_name=request.POST['first_name'])
    ninja.delete()
    return redirect('/')