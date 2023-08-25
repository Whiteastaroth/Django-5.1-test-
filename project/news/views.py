from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import New
from .forms import NewForm
from .filters import NewFilter
from django.urls import reverse_lazy


class NewList(ListView):
    model = New
    template_name = 'new/index.html'
    ordering = ['-date']
    ontext_object_name = 'new'
    paginate_by = 10

class SearchList(ListView):
    model = New
    ordering = ['-date']
    template_name = 'new/search.html'
    context_object_name = 'new'
    paginate_by = 10



    def get_filter(self):
        return NewFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        return {**super().get_context_data(*args, **kwargs), 'filter': self.get_filter(), }

class Newid(DetailView):
    model = New
    template_name = 'new/news_id.html'
    context_object_name = 'new'

class NewCreate(PermissionRequiredMixin,  CreateView):
    permission_required = ('news.add_new',)
    model = New
    form_class = NewForm
    template_name = 'new/create.html'


class NewUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_record',)
    model = New
    form_class = NewForm
    template_name = 'new/create.html'
    success_url = reverse_lazy('index')

class NewDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_record',)
    model = New
    template_name = 'new/news_delete.html'
    success_url = reverse_lazy('index')





