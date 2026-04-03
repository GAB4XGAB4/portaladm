from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Noticia, Cliente

def home(request):
    noticias = Noticia.objects.filter(ativo=True).order_by('-ordem', '-data_publicacao')
    context = {
        'noticias': noticias
    }
    return render(request, 'home.html', context)

def login_view(request):
    return render(request, 'login.html')

def contact(request):
    return HttpResponse("This is the contact page.")

def about(request):
    return HttpResponse("This is the about page.")