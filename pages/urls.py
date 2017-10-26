from django.conf.urls import url
from . import views

appname = 'pages'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.search, name='search'),
    url(r'^(?P<parent_location>\S*/)(?P<slug>\S+/)$', views.page, name='page'),
]
