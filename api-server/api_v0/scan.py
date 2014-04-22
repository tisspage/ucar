#!/usr/bin/env python
# encoding: utf-8
"""
scan.py

Created by Christophe VAN FRACKEM / Bastien ARNETTE on 2014/04/21/.
Copyright (c) 2014 Tiss'Page. MIT Licence.

Script listant les fichiers de la médiathèque. 

"""
__author__ = 'Christophe VAN FRACKEM <contact@tisspage.fr> / Bastien ARNETTE <bastien@rnette.fr>'
__version__= '0.0.1'
__copyright__ = '© 2014 Tiss\'Page for UCAR'

import os, os.path

from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC
from mutagen.mp3 import MP3

def scan_path(path, db, extensions):
	liste_fichier=[]
	separ=';'
	f=open(db,'w')

	for root, dirs, files in os.walk(path):
		for name in files:
			ext=os.path.splitext(name)
			ext=ext[1].lower()
			print ext
			if ext in extensions:
				
				print ext
				if ext =='.mp3':
					print ext
					try :
						audio = MP3(os.path.join(root,name), ID3=EasyID3)
					except: 
						print u'Le fichier %s n\'a pas été traité' %(os.path.join(root,name))
					ret = '%s %s' % (os.path.join(root,name).encode('utf-8'), separ)
					f.write(ret)
					ret =''

					if 'artist' in audio:
						ret += '%s %s' % (audio['artist'][0].encode('utf-8'),separ)
					else : 
						ret += '%s' % (separ)

					if 'title' in audio:
						ret += '%s %s' % (audio['title'][0].encode('utf-8'),separ)
					else : 
						ret += '%s' % (separ)

					if 'album' in audio:
						ret += '%s %s' % (audio['album'][0].encode('utf-8'),separ)
					else : 
						ret += '%s' % (separ)

					if 'date' in audio:
						ret += '%s %s' % (audio['date'][0].encode('utf-8'),separ)
					else : 
						ret += '%s' % (separ)

					if 'genre' in audio:
						ret += '%s %s' % (audio['genre'][0].encode('utf-8'),separ)
					else : 
						ret += '%s' % (separ)

					if 'tracknumber' in audio:
						ret += '%s %s' % (audio['tracknumber'][0].encode('utf-8'),separ)
					else : 
						ret += '%s' % (separ)

					f.write(ret)
					size = os.path.getsize(os.path.join(root,name))
					val1='%s %s %s \n' % (size/(1024),separ,int(audio.info.length))

					f.write(val1)
				
	f.close()
	return True
