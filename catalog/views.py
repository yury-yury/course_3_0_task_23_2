from typing import Dict, Any

from django.shortcuts import render

from catalog.models import Product, Contact


def main(request):
    if request.method == 'GET':
        result = Product.objects.all()
        print(result[:5])
        return render(request, 'catalog/home.html')


def contact(request):
    if request.method == 'POST':
        visiter: Dict[str, Any] = dict()
        visiter['name'] = request.POST.get('name', None)
        visiter['phone'] = request.POST.get('phone', None)
        visiter['message'] = request.POST.get('message', None)
        print(visiter)

    data: Dict[str, Any] = {"data": Contact.objects.get(pk=1)}
    return render(request, 'catalog/contact.html', context=data)
