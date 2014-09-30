from django.conf.urls import patterns, include, url
from django.contrib import admin
from classlists.views import ClassesListListView, StudentListListView
#from django.views.generic.base import TemplateView

urlpatterns = patterns('',
    url(r'^$',ClassesListListView.as_view(),name='classeslist_listview'),
    url(r'^(?P<klass>\w+)/$',StudentListListView.as_view(),name='studentlist_listview'),
)
