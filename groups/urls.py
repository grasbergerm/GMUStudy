from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^group/new/$', views.group_new, name='group_new'),
    url(r'^group/(?P<pk>[0-9]+)/$', views.group_detail, name='group_detail'),
    url(r'^groups/$', views.group_list, name='group_list'),
]
