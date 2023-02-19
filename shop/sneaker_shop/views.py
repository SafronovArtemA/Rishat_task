from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
import stripe
import os
from dotenv import load_dotenv, find_dotenv
import requests

currencies = {'1': 'RUB', '2': 'USD'}

load_dotenv(find_dotenv())

stripe.api_key = os.getenv('API_KEY')


def item(request, pk):
    data = get_object_or_404(Item, pk=pk)
    if request.method == 'GET':
        return render(request, 'sneaker_shop/item.html', {'data': data})


def buy(request, pk):
    currency = currencies[request.GET.get("currency")]
    data = get_object_or_404(Item, pk=pk)
    if currency not in 'RUB':
        rate = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()['Valute'][currency]['Value']
        price = int(data.price / rate * 100)
    else:
        price = int(data.price * 100)
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': currency,
                'product_data': {
                    'name': data.name,
                },
                'unit_amount': price,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=f'http://localhost:8000/item/{data.id}',
        cancel_url=f'http://localhost:8000/item/{data.id}',
    )

    return redirect(session.url, code=303)
