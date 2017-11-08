from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from .models import work, worker


class IndexView(generic.ListView):
    template_name = 'contractor/index.html'

    def get_queryset(self):
        return work.objects.all()


class DetailView(generic.DetailView):
    model = work
    template_name = 'contractor/detail.html'