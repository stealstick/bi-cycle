from django.conf.urls import include, url
from . import views

urlpatterns = [
     url(
        r'^login/',  views.login, name="login"
    ),
    url(
        r'^logout/',
        views.logout,
        name='logout',
    ),
    url(r'^signup/$', views.signup),
    url(r'^useradd$', views.useradd),   
]