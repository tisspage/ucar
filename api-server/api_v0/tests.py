#!/usr/bin/env python
# encoding: utf-8
"""
test.py

Created by Frédéric LASNIER / Christophe VAN FRACKEM on 2014/02/02/.
Copyright (c) 2014 Où & Quand. All rights reserved.

This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.

"""
__author__ = 'Frédéric LASNIER <fred@ouetquand.biz> / Christophe VAN FRACKEM <contact@tisspage.fr>'
__version__= '0.0.1'
__copyright__ = '© 2014 Où & Quand Pour Mécanicadom'

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
