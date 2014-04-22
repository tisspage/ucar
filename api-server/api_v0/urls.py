#!/usr/bin/env python
# encoding: utf-8
"""
urls.py

Created by Christophe VAN FRACKEM / Bastien ARNETTE on 2014/04/21/.
Copyright (c) 2014 Tiss'Page. MIT Licence.

UCAR API V.0 url. 

"""
__author__ = 'Christophe VAN FRACKEM <contact@tisspage.fr> / Bastien ARNETTE <bastien@rnette.fr>'
__version__= '0.0.1'
__copyright__ = '© 2014 Tiss\'Page for UCAR'

from django.conf.urls import patterns, include, url

#import generic views
from api_v0 import views

#from .views import UserListView, UserDetailView
#from .views import VehiculeListUserView, AdresseListUserView

urlpatterns = patterns('',
	url(r'^refresh$', views.RefreshList.as_view()),
	url(r'^files$', views.FileList.as_view()),
	url(r'^files/(?P<pk>\d+)$', views.FileDetail.as_view()),
	url(r'^sync$', views.SyncList.as_view()),
	#url(r'^users/(?P<pk>\d+)/adresses$', views.AdresseListUser.as_view()),

	#url(r'^supplier$', views.SupplierList.as_view()),

	#url(r'^customer$', views.CustomerList.as_view()),

	#url(r'^vehicules/(?P<pk>\d+)/$', views.VehiculeDetail.as_view()),
	#url(r'^vehicules$', views.VehiculeList.as_view()),

	#url(r'^adresses$', views.AdresseList.as_view()),
	#url(r'^adresses/(?P<pk>\d+)/$', views.AdresseDetail.as_view()),
	

    #[racine api]/users retourne tous les users selon les droits
    #[racine api]/users/:idUser (POST, GET, PUT, DELETE) selon les droits
    #[racine api]/users/:idUser/vehicules/ retourne tous les véhicules selon les droits
    #[racine api]/users/:idUser/adresses/ retourne toutes les adresses selon les droits
    #Les autres...
    url(r'^api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),

)
