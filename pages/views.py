from django.shortcuts import render
from .models import Page

def index(request):
    home = Page.objects.get(slug='home')
    return render(request, 'pages/' + home.template + '.html', home)

def search(request):
    search = Page.objects.get(slug='home')
    return render(request, 'pages/' + home.template + '.html', home)

def page(request, parent_location='', slug=''):
    page = Page.objects.get(slug=slug)
    return render(request, 'pages/' + page.template + '.html', page)
