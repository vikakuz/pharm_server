from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<drug_name>[-_0-9a-zA-ZА-Яа-я)(]+)/$', views.search_detail, name='search_detail'),
]