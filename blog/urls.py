from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
	url(r'^$', views.post_list),
	url(r'^blog/(?P<id>[0-9]+)/$', views.post_detail),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<id>[0-9]+)/edit/$', views.post_edit,  name='post_edit'),
	url(r'^post/(?P<id>[0-9]+)/publish/$', views.post_publish, name='post_publish'),
	url(r'^post/(?P<id>[0-9]+)/remove/$', views.post_remove, name='post_remove'),
	url(r'^post/draft/$', views.post_draft, name='post_draft'),
)