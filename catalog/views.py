from typing import Dict, Any
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Product, Contact

ITEM_ON_PAGE = 4


# def main(request):
#     if request.method == 'GET':
#         result = Product.objects.all()
#
#         paginator = Paginator(result, ITEM_ON_PAGE)
#         page_number = int(request.GET.get("page", 1))
#         page_object = paginator.get_page(page_number)
#
#         context = {"data": page_object,
#                    "page": page_number,
#                    "title": f"Каталог товаров, стр. {page_number} из {paginator.num_pages}"}
#         current_page = paginator.page(page_number)
#         if current_page.has_next():
#             context["next_page"] = current_page.next_page_number()
#         if current_page.has_previous():
#             context["previous_page"] = current_page.previous_page_number()
#
#         return render(request, 'catalog/home.html', context)


def contact(request):
    if request.method == 'POST':
        visiter: Dict[str, Any] = dict()
        visiter['name'] = request.POST.get('name', None)
        visiter['phone'] = request.POST.get('phone', None)
        visiter['message'] = request.POST.get('message', None)
        print(visiter)

    data: Dict[str, Any] = {"data": Contact.objects.get(pk=1), "title": "Контакты"}
    return render(request, 'catalog/contact.html', context=data)


# def detail_product(request, pk: int):
#     if request.method == 'GET':
#         product = Product.objects.get(pk=pk)
#         data: Dict[str, Any] = {"data": product, "title": "Информация о товаре"}
#         return render(request, 'catalog/product_detail.html', context=data)


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    paginate_by = ITEM_ON_PAGE


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
