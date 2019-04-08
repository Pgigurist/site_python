from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.MKList, name='mk_list'),
    url(r'^(?P<question_id>[0-9]+)/$', views.MKDetalis, name='detalis'),
    url(r'^landing/$', views.Landing, name='landing'),
]
