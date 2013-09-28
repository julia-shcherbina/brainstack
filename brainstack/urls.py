from django.conf.urls import patterns, include, url

from core.views import MainTemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
        url(r'^$', MainTemplateView.as_view(), name='index'),
)
