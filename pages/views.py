from django.shortcuts import render
from .models import Page

def index(request):
    page = Page.objects.get(slug='home')
    context = {'page': page}
    return render(request, 'pages/' + page.template + '.html', context)

def search(request):
    page = Page.objects.get(slug='home')
    context = {'page': page}
    return render(request, 'pages/' + page.template + '.html', context)

def page(request, location=''):
    location = location.split('/')
    page = Page.objects.get(slug=location[-1])
    context = {'page': page}
    return render(request, 'pages/' + page.template + '.html', context)
