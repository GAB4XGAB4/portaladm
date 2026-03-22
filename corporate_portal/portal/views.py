from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'base.html')

def about(request):
    return HttpResponse("This is the about page.")