#!/usr/bin/env python
# encoding: utf-8
"""
admin.py

Created by Christophe VAN FRACKEM / Bastien ARNETTE on 2014/04/21/.
Copyright (c) 2014 Tiss'Page. MIT Licence.

UCAR admin models. 

"""
__author__ = 'Christophe VAN FRACKEM <contact@tisspage.fr> / Bastien ARNETTE <bastien@rnette.fr>'
__version__= '0.0.1'
__copyright__ = '© 2014 Tiss\'Page for UCAR'

from django.contrib import admin
from api_v0.models import Synchro, Extension, Categorie, Infos, File, Configuration, Cible

admin.site.register(Synchro)
admin.site.register(Extension)
admin.site.register(Categorie)
admin.site.register(Infos)
admin.site.register(File)
admin.site.register(Configuration)
admin.site.register(Cible)