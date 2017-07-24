from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^returnitem$', views.returnitem),
    url(r'^send/(?P<username>.+)/$', views.send),
    url(r'^borrow/$', views.borrow),
    url(r'^sending/(?P<username>.+)/$', views.sending),
    url(r'^category/(?P<category>.+)/$', views.category),
    url(r'^delete/$', views.delete),
    url(r'^search/$', views.search),
]
