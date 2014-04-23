#!/usr/bin/env python
# encoding: utf-8
"""
views.py

Created by Christophe VAN FRACKEM / Bastien ARNETTE on 2014/04/21/.
Copyright (c) 2014 Tiss'Page. MIT Licence.

UCAR generics views. 

"""
__author__ = 'Christophe VAN FRACKEM <contact@tisspage.fr> / Bastien ARNETTE <bastien@rnette.fr>'
__version__= '0.0.1'
__copyright__ = '© 2014 Tiss\'Page for UCAR'

import os, os.path, csv

from django.views.generic import View, TemplateView, FormView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.list import ListView
from django.http import Http404

from rest_framework import mixins, generics

#from api_v0.permissions import FilePerm
from api_v0.models import Synchro, Extension, Categorie, Infos, File, Configuration, Cible
from api_v0.scan import scan_path
from api_v0.serializers.file import FileSerializer



class SyncList(View):
	
	def get(self, request, *args, **kwargs):
		file_to_remove = File.objects.filter(futur_state = 'no-sync') 	#recupère la liste des fichiers à supprimer de la cible
		file_to_add = File.objects.filter(futur_state ='sync') 			#recupère la liste des fichiers à ajouter à la cible

		#####################################################################
		# 																 	#
		#																	#
		#	ICI script pour lancer la commande de synchro avec la cible.	#
		#																	#
		#																	#
		#																	#
		#####################################################################


		return True

####################### SCAN ##################################
class RefreshList(View):
	pathtoscan='/home/chrisbian/Musique/'
	scanfinished = '/tmp/audio.csv' #path rep temporaire
	extensions = ['.flac', '.mp3',] #extensions autorisées

	def get(self, request, *args, **kwargs):
		configuration = Configuration.objects.all()
		if len(configuration)>0:
			configuration = Configuration.objects.all()[0]
		if configuration : 
			if configuration.pathtoscan != '':
				self.pathtoscan = configuration.pathtoscan
			if configuration.authorized_ext != '':
				extension = configuration.authorized_ext.all()
				self.extensions =['',]
				for ext in extension:
					self.extensions.append(str(ext.ext))

		scan_path(self.pathtoscan, self.scanfinished, self.extensions)
		with open(self.scanfinished) as f:
			reader = csv.reader(f, delimiter=';')
			for row in reader:
				_, created = File.objects.get_or_create(
															categorie=Categorie.objects.get(title = "audio"),
															path=row[0],
															info=Infos.objects.create(
																artist = row[1],
																title = row[2],
																album = row[3],
																date = row[4],
																genre = row[5],
																tracknumber = row[6],
																length = row[7],
																size = row[8],
																),
															)
				# creates a tuple of the new object or
				# current object and a boolean of if it was created
			f.close()

		## PENSER A SUPPRIMER LE FICHIER TEMPORAIRE ##
		return True

		


####################### FILE ##################################
class FileMixin(object):
	queryset = File.objects.all() 
	serializer_class = FileSerializer
	#permission_classes = (FilePerm, )

class FileList(FileMixin, generics.ListCreateAPIView):
	pass

class FileDetail(FileMixin, generics.RetrieveUpdateDestroyAPIView):
	pass


class DashBoardView(TemplateView):
	template_name = 'dashboard.html'

class ListView(TemplateView):
	template_name = 'list-files.html'