__author__ = 'shixiaokun'

from django.conf.urls import patterns, url, include

urlpatterns = patterns('userinfo.views',
    url(r'^register$', 'register'),
    url(r'^submitregister$', 'submitregister'),
)