from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.MKList, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.MKDetalis, name='detalis'),
    url(r'^landing/$', views.Landing, name='landing'),
]
