from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^(?P<cloth_name>.+)$', views.index),
]
