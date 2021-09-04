# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 09:57:52 2020

@author: dell
"""
import os

filelist = os.listdir('E://刘天旭的资料/纪念册/照片')
path = 'E://刘天旭的资料/纪念册/照片/'
totalnum = len(filelist)
num = 1
for filename in filelist:
    oldname = path + filename
    newname = path+str(num)+'.jpg'
    os.rename(oldname,newname)
    num = num + 1