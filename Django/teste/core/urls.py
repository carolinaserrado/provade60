from django.urls import path
from .views import *
from core import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('contato', contato, name = 'contato'),
    path('produto/<int:id>', produto, name = 'produto')
]

handler404 = views.error404
handler500 = views.error500