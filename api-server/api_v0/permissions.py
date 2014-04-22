#!/usr/bin/env python
# encoding: utf-8
"""
permissions.py

Created by Frédéric LASNIER / Christophe VAN FRACKEM on 2014/02/02/.
Copyright (c) 2014 Où & Quand. All rights reserved.

Mecanicadom permission. 

"""
__author__ = 'Frédéric LASNIER <fred@ouetquand.biz> / Christophe VAN FRACKEM <contact@tisspage.fr>'
__version__= '0.0.1'
__copyright__ = '© 2014 Où & Quand Pour Mécanicadom'

# Import #
from rest_framework.permissions import BasePermission, SAFE_METHODS

from django.contrib.auth.models import User

class AdressePerm(BasePermission):
	SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']
	#Permission for detail object
	def has_object_permission(self, request, view, obj):
		utilisateur = Utilisateur.objects.filter(username = request.user.username)
		util = ''
		if len(utilisateur) > 0:
			util = Utilisateur.objects.get(username = request.user.username)

		if request.method in self.SAFE_METHODS:
			return True
		elif request.method == 'DELETE':
			if util != '':
				if util.usr_cat == 'admin-tech':
					return True

		elif request.method == 'PUT':
			if util != '':
				if (util.usr_cat == 'admin-tech') or (util.usr_cat == 'admin-ceo') or (obj.created_by == util) :
					return True

		elif request.method == 'POST':
			if util != '':
				if (util.usr_cat == 'admin-tech') or (util.usr_cat == 'admin-ceo'):
					return True

		elif request.method == 'PATCH':
			if util != '':
				if util.usr_cat == 'admin-tech':
					return True

		return obj.created_by == request.user

	#Permission for list object
	def has_permission(self, request, view):
		utilisateur = Utilisateur.objects.filter(username = request.user.username)
		util = ''
		if len(utilisateur) > 0:
			util = Utilisateur.objects.get(username = request.user.username)

		if request.method in self.SAFE_METHODS:
			return True
		elif request.method == 'DELETE':
			if util != '':
				if util.usr_cat == 'admin-tech':
					return True
				else: 
					return False

		elif request.method == 'PUT':
			if util != '':
				if (util.usr_cat == 'admin-tech') or (util.usr_cat == 'admin-ceo') :
					return True
				else: 
					return False

		elif request.method == 'POST':
			if util != '':
				if (util.usr_cat == 'admin-tech') or (util.usr_cat == 'admin-ceo'):
					return True
				else: 
					return False

		elif request.method == 'PATCH':
			if util != '':
				if util.usr_cat == 'admin-tech':
					return True
				else: 
					return False

		return True

class UtilisateurPerm(BasePermission):
	SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']
	#Permission for detail object
	def has_object_permission(self, request, view, obj):
		utilisateur = Utilisateur.objects.filter(username = request.user.username)
		util = ''
		if len(utilisateur) > 0:
			util = Utilisateur.objects.get(username = request.user.username)

		if request.method in self.SAFE_METHODS:
			return True
		elif request.method == 'DELETE':
			if util != '':
				if util.usr_cat == 'admin-tech':
					return True

		elif request.method == 'PUT':
			if util != '':
				if (util.usr_cat == 'admin-tech') or (util.usr_cat == 'admin-ceo') or (obj.created_by == util) :
					return True

		elif request.method == 'POST':
			if util != '':
				if (util.usr_cat == 'admin-tech') or (util.usr_cat == 'admin-ceo'):
					return True

		elif request.method == 'PATCH':
			if util != '':
				if util.usr_cat == 'admin-tech':
					return True

		return obj.created_by == request.user

	#Permission for list object
	def has_permission(self, request, view):
		utilisateur = Utilisateur.objects.filter(username = request.user.username)
		util = ''
		if len(utilisateur) > 0:
			util = Utilisateur.objects.get(username = request.user.username)

		if request.method in self.SAFE_METHODS:
			return True
		elif request.method == 'DELETE':
			if util != '':
				if util.usr_cat == 'admin-tech':
					return True
				else: 
					return False

		elif request.method == 'PUT':
			if util != '':
				if (util.usr_cat == 'admin-tech') or (util.usr_cat == 'admin-ceo') :
					return True
				else: 
					return False

		elif request.method == 'POST':
			if util != '':
				if (util.usr_cat == 'admin-tech') or (util.usr_cat == 'admin-ceo'):
					return True
				else: 
					return False

		elif request.method == 'PATCH':
			if util != '':
				if util.usr_cat == 'admin-tech':
					return True
				else: 
					return False

		return True

class VehiculePerm(BasePermission):
	SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']
	#Permission for detail object
	def has_object_permission(self, request, view, obj):
		utilisateur = Utilisateur.objects.filter(username = request.user.username)
		util = ''
		if len(utilisateur) > 0:
			util = Utilisateur.objects.get(username = request.user.username)

		if request.method in self.SAFE_METHODS:
			return True
		elif request.method == 'DELETE':
			if util != '':
				if util.usr_cat == 'admin-tech':
					return True

		elif request.method == 'PUT':
			if util != '':
				if (util.usr_cat == 'admin-tech') or (util.usr_cat == 'admin-ceo') or (obj.created_by == util) :
					return True

		elif request.method == 'POST':
			if util != '':
				if (util.usr_cat == 'admin-tech') or (util.usr_cat == 'admin-ceo'):
					return True

		elif request.method == 'PATCH':
			if util != '':
				if util.usr_cat == 'admin-tech':
					return True

		return obj.created_by == request.user

	#Permission for list object
	def has_permission(self, request, view):
		utilisateur = Utilisateur.objects.filter(username = request.user.username)
		util = ''
		if len(utilisateur) > 0:
			util = Utilisateur.objects.get(username = request.user.username)

		if request.method in self.SAFE_METHODS:
			return True
		elif request.method == 'DELETE':
			if util != '':
				if util.usr_cat == 'admin-tech':
					return True
				else: 
					return False

		elif request.method == 'PUT':
			if util != '':
				if (util.usr_cat == 'admin-tech') or (util.usr_cat == 'admin-ceo') :
					return True
				else: 
					return False

		elif request.method == 'POST':
			if util != '':
				if (util.usr_cat == 'admin-tech') or (util.usr_cat == 'admin-ceo'):
					return True
				else: 
					return False

		elif request.method == 'PATCH':
			if util != '':
				if util.usr_cat == 'admin-tech':
					return True
				else: 
					return False

		return True
	
