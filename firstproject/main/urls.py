from django.urls import path
from django.http import HttpResponse
from .views import AdvertListView, AdvertDetailView, AdvertCreate


def testView(request):
    """
    Текстовый метод для проверки запуска тестовой страницы.
    """
    return HttpResponse('<div align="center"><h1 style="color:red">Это тестовая страница!</h1></div>')


urlpatterns = [
    path('', AdvertListView.as_view(), name='adv_list'),
    path('detail/<int:pk>', AdvertDetailView.as_view(), name='adv.detail'),
    path('create/', AdvertCreate.as_view(), name='adv.create'),
]
