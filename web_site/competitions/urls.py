from django.conf.urls import url
from . import views

#SET NAMESPACE  чтобы не писать через точку
app_name = 'competitions'

urlpatterns = [
    url(r'^$', views.index, name='main'), #index
]
