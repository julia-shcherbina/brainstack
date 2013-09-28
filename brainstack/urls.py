from django.conf.urls import patterns, include, url

from core.views import HomeView, SPAView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^spa/(?P<project_id>\w+)$', SPAView.as_view(), name='spa'),
    url(r'^api/', include('api.urls', namespace='api')),

)
