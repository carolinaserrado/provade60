from django.shortcuts import render
from django.template import context
from .models import Produto

# Create your views here.

def index(request):
    produtos = Produto.objects.all()
    context = {
        'produtos' : produtos,
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, id):
    prod = Produto.objects.get(id=id)
    context = {
        'produto' : prod
    }
    return render(request, 'produto.html', context)

def error404(request, exception):
    return render(request, '404.html')

def error500(request):
    return render(request, '500.html')