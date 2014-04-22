#!/usr/bin/env python
# encoding: utf-8
"""
urls.py

Created by Christophe VAN FRACKEM / Bastien ARNETTE on 2014/04/21/.
Copyright (c) 2014 Tiss'Page. MIT Licence.

URL globaux UCAR

"""
__author__ = 'Christophe VAN FRACKEM <contact@tisspage.fr> / Bastien ARNETTE <bastien@rnette.fr>'
__version__= '0.0.1'
__copyright__ = '© 2014 Tiss\'Page for UCAR'

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mad.views.home', name='home'),
    # url(r'^mad/', include('mad.foo.urls')),
    url(r'^api/v0/', include('api_v0.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
