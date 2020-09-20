from django.shortcuts import render, redirect
from random import randrange
from datetime import datetime

locations = {
    "farm": [10,20],
    "cave": [5,10],
    "house": [2,5],
    "casino": [-3, 3]
}

# Create your views here.
def index (request):
    if 'gold' not in request.session or 'activities' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
    return render (request, 'index.html')

def process_money (request):
    if request.method == "GET":
        return redirect('/')
    
    location_name = request.POST['location']
    location = locations[location_name]
    now = datetime.now().strftime("%m/%d/%Y %I:%M%p")
    amount = int(randrange(location[0], location[1], 1)) 

    if location_name == 'casino':
        result = "won"
        bet = int(request.POST['bet_amount'])
        if bet < 1:
            bet = 1
        amount = bet * amount
        if amount<0:
            result='lost' 
        request.session['gold'] = request.session['gold'] + amount

    else:
        request.session['gold']=request.session['gold'] + amount
        if location_name == "farm":
            result = "earn"  
        else:
            result = "found"

    message = f"You {result} {amount} gold at the {location_name}! {now}"
    request.session['activities'].append({"message": message, "result": result})
    
    return redirect('/')

def destroy (request):
    request.session.clear()
    return redirect('/')