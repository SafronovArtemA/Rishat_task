from django.shortcuts import render, get_object_or_404
from .models import Item
from .forms import ItemForm


def item(request, pk):
    el = get_object_or_404(Item, pk=pk)
    if request.method == 'GET':
        data = ItemForm(instance=el)
        return render(request, 'sneaker_shop/item.html', {'data':data})
