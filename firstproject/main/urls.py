from django.urls import path
from django.http import HttpResponse
from .views import AdvertListView


def testView():
    return HttpResponse('<div align="center"><h1 style="color:red">Это тестовая страница!</h1></div>')


urlpatterns = [
    path('main/', AdvertListView.as_view(), name='adv_list')
]
