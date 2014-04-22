#!/usr/bin/env python
# encoding: utf-8
"""
__init__.py

Created by Christophe VAN FRACKEM / Bastien ARNETTE on 2014/04/21/.
Copyright (c) 2014 Tiss'Page. MIT Licence.

UCAR base models. 

"""
__author__ = 'Christophe VAN FRACKEM <contact@tisspage.fr> / Bastien ARNETTE <bastien@rnette.fr>'
__version__= '0.0.1'
__copyright__ = '© 2014 Tiss\'Page for UCAR'

# - Import - #
from django.db import models
from datetime import datetime

class Synchro(models.Model):
	ETAT = (
		('no-sync','Non Synchronisé'),
		('sync','Synchronisé'),
		)
	actual_state = models.CharField(max_length=255, choices=ETAT)
	futur_state = models.CharField(max_length=255, choices=ETAT, null = True, blank = True)
	date_sync = models.DateTimeField()
	
	def save(self, *args, **kwargs):
		# - set datetime on save or modify- #
		self.date_sync = datetime.now()
		self.actual_state = 'no-sync'
		super(Synchro, self).save(*args, **kwargs)

	def __unicode__(self):
		return unicode(self.actual_state)
	class Meta:
		ordering = ['actual_state']

class Extension(models.Model):
	ext = models.CharField(max_length=15)

	def __unicode__(self):
		return unicode(self.ext)
	class Meta:
		ordering = ['ext']

class Categorie(models.Model):
	title = models.CharField(max_length=255)
	extension = models.ManyToManyField(Extension)

	def __unicode__(self):
		return unicode(self.title)
	class Meta:
		ordering = ['title']

class Infos(models.Model): 
	artist = models.CharField(max_length=255, null = True, blank = True)
	title = models.CharField(max_length=255, null = True, blank = True)
	album = models.CharField(max_length=255, null = True, blank = True)
	date = models.CharField(max_length=255, null = True, blank = True)
	genre = models.CharField(max_length=255, null = True, blank = True)
	tracknumber = models.CharField(max_length=255, null = True, blank = True)
	length = models.IntegerField( null = True, blank = True)
	size = models.IntegerField( null = True, blank = True)

	def __unicode__(self):
		return unicode(''.join( self.artist +' - '+ self.title + '(album : '+ self.album + ')'))
	class Meta:
		ordering = ['artist']

class File(Synchro):
	categorie = models.ForeignKey(Categorie)
	path = models.CharField(max_length=5000)
	info = models.ForeignKey(Infos)

	def __unicode__(self):
		return unicode(self.path)
	class Meta:
		ordering = ['categorie']

class Configuration(models.Model):
	pathtoscan = models.CharField(max_length=5000, null = True, blank = True)
	authorized_ext = models.ManyToManyField(Extension, null = True, blank = True)

class Cible(models.Model):
	name = models.CharField(max_length=255)
	ip = models.GenericIPAddressField()
	default = models.BooleanField(default=True)
	connected = models.BooleanField(default = False)
	last_sync = models.DateTimeField()
	space_storage_size = models.IntegerField()
	space_free_size = models.IntegerField()
	path_to_sync = models.CharField(max_length=5000)

	def __unicode__(self):
		return unicode(''.join( self.name +' - '+ self.ip))
	class Meta:
		ordering = ['last_sync']