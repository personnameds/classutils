from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = patterns('',
    url(r'^$',TemplateView.as_view(template_name='index.html')),
    url(r'^classes/', include('classlists.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
