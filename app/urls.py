from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^convert/$', views.convert, name='convert'),
    url(r'^get_currencies/$', views.get_currencies, name='get_currencies'),
]