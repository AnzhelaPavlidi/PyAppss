from django.shortcuts import render
from django.views import generic
from .models import Advert


class AdvertListView(generic.ListView):
    """
    Список рекламных обьявлений
    """
    queryset = Advert.objects.all()
    template_name = "main/advertlist.html"
    context_object_name = 'adv'


class AdvertDetailView(generic.DetailView):
    model = Advert
    template_name = "main/advertdetail.html"
    context_object_name = 'adv'


class AdvertCreate(generic.CreateView):
    form_class = AdvertForm
    template_name = 'main/advertcreate.html'
