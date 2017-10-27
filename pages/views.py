from django.shortcuts import render
from django.utils import timezone
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
    children = Page.objects.filter(parent = page, pub_date__lte=timezone.now())
    context = {'page': page, 'children': children}
    return render(request, 'pages/' + page.template + '.html', context)
