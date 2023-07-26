from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogEntryCreateView, BlogEntryListView, BlogEntryDetailView, BlogEntryUpdateView
from blog.views import BlogEntryDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogEntryCreateView.as_view(), name='create'),
    path('list/', BlogEntryListView.as_view(), name='list'),
    path('detail/<int:pk>', BlogEntryDetailView.as_view(), name='detail'),
    path('update/<int:pk>', BlogEntryUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BlogEntryDeleteView.as_view(), name='delete'),

]