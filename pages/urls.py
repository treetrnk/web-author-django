from django.conf.urls import url
from . import views

appname = 'pages'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.search, name='search'),
    url(r'^(?P<location>.*)/$', views.page, name='page'),
]
