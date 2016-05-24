from django.conf.urls import url, include
from rest_framework import routers
from . import views
# Wire up our API using automatic URL routing.


app_name='androider'
urlpatterns = [
    url(r'^$', views.device_list, name='device_list'),
    url(r'^?initialPoint=(?P<inicoord>[[-+]?[0-9]*\.?[0-9]+,[-+]?[0-9]*\.?[0-9]+])&?finalPoint=(?P<fincoord>[[-+]?[0-9]*\.?[0-9]+,[-+]?[0-9]*\.?[0-9]+])/coord/$', views.coord, name='coord'),
    url(r'^/dijk/$', views.dijk, name='dijk'),

]
