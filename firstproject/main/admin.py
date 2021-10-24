from django.contrib import admin
from .models import Advert, Photo

''' Нужно импортировать модель,чтобы она была тут доступна'''

admin.site.register(Advert)
''' Подключаем нашу модель Advert к админке'''

admin.site.register(Photo)
''' Подключаем нашу модель Photo к админке'''

