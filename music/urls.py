from django.conf.urls import url
from . import views

app_name = 'music'   # this app name is used for reference in templates especially when multiple apps have same url names.

urlpatterns = [
	# /music/
	url(r'^$', views.index, name = 'index'),# name help making the site more dynamic 
	 # /music/<album_id>/
	url(r'^(?P<album_id>[0-9]+)/$',views.detail, name='detail'),


	# this urls is made to perform a task and redirect to the same webpage as before 
	# URLs are also used to perform some task eg. LOGOUT
	# /music/<album_id>/favourite/
	url(r'^(?P<album_id>[0-9]+)/favorite/$',views.favorite, name='favorite'),
] 