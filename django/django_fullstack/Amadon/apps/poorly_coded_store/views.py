from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    product = Product.objects.get(id=request.POST["product_id"])
    quantity_from_form = int(request.POST["quantity"])
    price_from_form = float(product.price)
    total_charge = quantity_from_form * price_from_form
    print("Charging credit card...")
    order=Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return redirect("/checkout_confirm")

def checkout_confirm (request):
    total_spent=0.00
    total_quantity=0
    for charges in Order.objects.all():
        total_spent += float(charges.total_price)
        total_quantity += int(charges.quantity_ordered)
    context = {
        'order':Order.objects.order_by('-id')[0],
        "total_quantity":total_quantity,
        "total_spent":total_spent
    }
    return render (request, "store/checkout.html", context)