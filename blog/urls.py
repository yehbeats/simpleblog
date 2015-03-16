from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
	url(r'^$', views.post_list),
	url(r'^blog/(?P<id>[0-9]+)/$', views.post_detail),
)