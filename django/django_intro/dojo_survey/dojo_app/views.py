from django.shortcuts import render, redirect

# Create your views here.
def index (request):
    if request.method =="GET":
        return render(request, "index.html")
    if request.method == "POST":
        return redirect('/other_page')

def other_page (request):
    if request.method == "POST":
        context = {
            "name": request.POST['name'],
            "location": request.POST['location'],
            "language": request.POST['language'],
            "comment": request.POST['comment']
    }
    return render(request, "other_page.html", context)