from django.conf.urls import url
from . import views          
urlpatterns = [
    url(r'^$', views.home),
    url(r'^home$', views.home),
    url(r'^menu$', views.menu),
    url(r'^hours$', views.hours),
]    