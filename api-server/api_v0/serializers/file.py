#!/usr/bin/env python
# encoding: utf-8
"""
serializers.py

Created by Christophe VAN FRACKEM / Bastien ARNETTE on 2014/04/21/.
Copyright (c) 2014 Tiss'Page. MIT Licence.

UCAR serializers. 

"""
__author__ = 'Christophe VAN FRACKEM <contact@tisspage.fr> / Bastien ARNETTE <bastien@rnette.fr>'
__version__= '0.0.1'
__copyright__ = '© 2014 Tiss\'Page for UCAR'


from rest_framework import serializers
from api_v0.models import File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File