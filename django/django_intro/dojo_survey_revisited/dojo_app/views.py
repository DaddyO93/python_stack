from django.shortcuts import render, redirect

# Create your views here.
def index (request):
    if request.method =="GET":
        return render(request, "index.html")
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        return redirect('/other_page')

def other_page (request):
    return render(request, "other_page.html")