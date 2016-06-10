from django.conf.urls import patterns, include, url
from . import views


urlpatterns = patterns('',
					   url(r'^provider/$', views.CreateProvider.as_view()),
					   url(r'^provider/update/(?P<pk>[0-9]+)/$', views.ProviderUpdate.as_view()),
					   url(r'^provider/points/$', views.CreatePolygon.as_view()),
					   url(r'^provider/points/update/(?P<pk>[0-9]+)/$', views.PolygonUpdate.as_view()),
					   url(r'^provider/points/search/$', views.PolygonSearch.as_view()),
			)