from django.conf.urls import patterns, url, include

from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet)
print 'routs', router.get_routes('tasks')

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
