__author__ = 'shixiaokun'

from django.conf.urls import url, patterns

urlpatterns = patterns('article.views',
    url(r'^article$', 'article'),
)
