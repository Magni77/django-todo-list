
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.task_list, name='list'),
    url(r'^create/$', views.task_create, name='create'),
    url(r'^(?P<id>\d+)/$', views.task_details, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', views.task_edit, name='edit'),
    url(r'^(?P<id>\d+)/delete/$', views.delete_task, name='delete'),

]
