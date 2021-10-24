from django.shortcuts import render
from django.views import generic
from .models import Advert, Photo


class AdvertListView(generic.ListView):
    """
    Список рекламных обьявлений
    """
    queryset = Advert.objects.all()
    template_name = "main/advertlist.html"
    context_object_name = 'adv'


class AdvertDetailView(generic.DetailView):
    """ Детализированная форма обьявления"""
    model = Advert
    template_name = "main/advertdetail.html"
    context_object_name = 'adv'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photo'] = Photo.objects.filter(advert=self.kwargs['pk'])
        return context

class AdvertForm(object):
    pass


class AdvertCreate(generic.CreateView):
    form_class = AdvertForm
    template_name = 'main/advertcreate.html'


class AdvertUpdate(generic.UpdateView):
    model = Advert
    form_class = AdvertForm
    template_name = 'maim/advertupdate.html'
    context_object_name = 'adv'


class AdvertDelete(generic.DeleteView):
    model = Advert
    template_name = 'main/advert_confirm_delete.html'
    context_object_name = 'adv'
    success_url = '/'
