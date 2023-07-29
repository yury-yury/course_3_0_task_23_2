from typing import Dict, Any

from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Contact, Version

ITEM_ON_PAGE = 4


def contact(request):
    if request.method == 'POST':
        visiter: Dict[str, Any] = dict()
        visiter['name'] = request.POST.get('name', None)
        visiter['phone'] = request.POST.get('phone', None)
        visiter['message'] = request.POST.get('message', None)
        print(visiter)

    data: Dict[str, Any] = {"data": Contact.objects.get(pk=1), "title": "Контакты"}
    return render(request, 'catalog/contact.html', context=data)


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog')

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=None, **kwargs)
        data['title'] = "Создание новой карточки товара."
        return data


class ProductListView(ListView):
    model = Product
    paginate_by = ITEM_ON_PAGE

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=None, **kwargs)
        data['title'] = f"Каталог товаров, стр. {data['page_obj'].number} из {data['page_obj'].paginator.num_pages}"
        return data


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = f'Детальный просмотр продукта {data["object"].name}'
        return data


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:update', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        version_formset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            data['formset'] = version_formset(self.request.POST, instance=self.object)
        else:
            data['formset'] = version_formset(instance=self.object)
        data['title'] = f'Обновление карточки товара {data["object"].name}'

        return data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)



class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:catalog')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = f'Удаление карточки товара {data["object"].name}'
        return data

