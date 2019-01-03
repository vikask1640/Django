from django.conf.urls import url,include
from django.urls import path
from . import views
urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^contact/$', views.contact,name='contact'),


]
