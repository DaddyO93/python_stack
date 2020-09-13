from django.shortcuts import render
from time import localtime, strftime

# Create your views here.
def index (request):
    context = {
        "date": strftime('%b %d, %Y', localtime()),
        "time": strftime('%I:%m %p', localtime())
    }
    return render(request, 'index.html', context)