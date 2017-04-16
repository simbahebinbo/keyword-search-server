# coding=utf-8

from django.conf.urls import url
from .views import ApiSearch


urlpatterns = [
    url(r'search/$', ApiSearch.as_view(), name='search'),
]





