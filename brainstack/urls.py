from django.conf.urls import patterns, include, url

from core.views import MainTemplateView, SPAView

urlpatterns = patterns('',
    url(r'^$', MainTemplateView.as_view(), name='index'),
    url(r'^spa/(?P<project_id>\w+)$', SPAView.as_view(), name='spa'),
    url(r'^api/', include('api.urls', namespace='api')),

)
