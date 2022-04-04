from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KkuhiBJzeXq1XU5sEXIBWCGvyVamO8fZLqItjzlEqCJQL7P2zQGQIAEQvH6EiRMnP7GpFg6DICehDSqvmUpd1qH00aBmy7eKl',
        'client_secret': 'blablatest',
    }

    return render(request, template, context)
