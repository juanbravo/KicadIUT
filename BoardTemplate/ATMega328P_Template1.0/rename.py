#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import sys

myname=sys.argv[0]

dirbase = os.getcwd()
if dirbase.find('/') != -1 :
	newbasename=dirbase.split('/')[-1]
else:
	newbasename=dirbase.split('\\')[-1]
print(myname)
print('Rename to ',newbasename)
r=input('Continue ? (Y/n)')
if r not in ['','Y','y'] : 
  sys.exit()
for filename in os.listdir('.') :
     #~print('found : ',filename,end='')
     if os.path.isdir(filename) :
        #~print('dir')
        continue
     if (filename!=myname and filename!='rename.py') : 
        
        ext_index = filename[::-1].find('.')
        if (ext_index != -1) :
            ext = filename[-ext_index:] 
            #~print('extension : ', ext,end=' ')
            newname = newbasename + '.' + ext
            #~print(newname)
            os.rename(filename,newname)
          
for filename in os.listdir('.') :
     print(filename)
