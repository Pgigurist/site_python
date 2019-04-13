from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.MKList, name='mk_list'),
    url(r'^(?P<mk_id>[0-9]+)/$', views.MKDetalis, name='mk_id'),
    url(r'^landing/$', views.Landing, name='landing'),
    url(r'^signup/$', views.signup, name='signup'),

]
