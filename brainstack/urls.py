from django.conf.urls import patterns, include, url

from views import HelloView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HelloView.as_view(), name='hello'),
    #url(r'todo/^$', 'views.home', name=''),
)
