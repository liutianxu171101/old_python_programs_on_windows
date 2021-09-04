# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 15:56:06 2020

@author: dell
"""

import csv

data = []
path = 'E://Python/programs/热榜/'
file = 'Sat Sep 26 11 24 38 2020.csv'
f = open(path+file,'r',newline='',encoding='UTF-8')
csv_reader = csv.reader(f)
for row in csv_reader:
    if (row[1]=='热度'):
       continue
    else:
       data.append(int(row[1]))
f.close()