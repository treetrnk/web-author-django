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

def page(request, parent_location='', slug=''):
    page = Page.objects.get(slug=slug)
    context = {'page': page}
    return render(request, 'pages/' + page.template + '.html', context)
