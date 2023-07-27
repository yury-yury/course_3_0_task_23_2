from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import BlogEntry
from internet_shop.settings import DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL


ITEM_ON_PAGE = 4


class BlogEntryCreateView(CreateView):
    model = BlogEntry
    fields = ('title', 'content', 'preview')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid:
            new = form.save()
            new.slug = slugify(new.title)
            # new.slug = new.title.strip().lower().replace(' ', '_')
            new.save()
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=None, **kwargs)
        data['title'] = "Создание новой записи блога."
        return data


class BlogEntryListView(ListView):
    model = BlogEntry
    paginate_by = ITEM_ON_PAGE

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(published=True)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=None, **kwargs)
        data['title'] = f"Список записей блога, стр. {data['page_obj'].number} из {data['page_obj'].paginator.num_pages}"
        return data


class BlogEntryDetailView(DetailView):
    model = BlogEntry

    def get_object(self, queryset=None) -> BlogEntry:
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()

        if self.object.views_count == 100:
            send_mail('Поздравление!', f'Ваша запись блога {self.object.title} набрала 100 просмотров. Примите поздравления',
                      DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)

        return self.object

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = f'Просмотр записи блога {data["object"].title}'
        return data


class BlogEntryUpdateView(UpdateView):
    model = BlogEntry
    fields = ('title', 'content', 'preview', 'published')

    def form_valid(self, form):
        if form.is_valid:
            new = form.save()
            new.slug = slugify(new.title)
            new.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:detail', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = f'Редактирование записи блога {data["object"].title}'
        return data


class BlogEntryDeleteView(DeleteView):
    model = BlogEntry
    success_url = reverse_lazy('blog:list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = f'Удаление записи блога {data["object"].title}'
        return data
