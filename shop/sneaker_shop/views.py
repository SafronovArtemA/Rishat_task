from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
import stripe
from shop.settings import api_key

stripe.api_key = api_key


def item(request, pk):
    data = get_object_or_404(Item, pk=pk)
    if request.method == 'GET':
        return render(request, 'sneaker_shop/item.html', {'data': data})


def buy(request, pk):
    data = get_object_or_404(Item, pk=pk)
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'rub',
                'product_data': {
                    'name': data.name,
                },
                'unit_amount': int(data.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=f'http://localhost:8000/item/{data.id}',
        cancel_url=f'http://localhost:8000/item/{data.id}',
    )

    return redirect(session.url, code=303)
