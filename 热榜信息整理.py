# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 11:09:16 2020

@author: dell
"""

import os
import csv
from matplotlib import pyplot as plt

path = 'E://Python/programs/热榜/'
filelist = os.listdir(path)
time = []
data = []
titles = [' ']
#第一次遍历，找出所有的标题
isin = 0
for file in filelist:
    time.append(file[11:19])
    f = open(path+file,'r',newline='',encoding='UTF-8')
    csv_reader = csv.reader(f)
    for row in csv_reader:
        loc = 0
        if (row[1]=='热度'):
            continue
        else:
            for title in titles:
               if (title == row[0]):
                   isin = 1
                   break
            if isin == 0:
                titles.append(row[0])
            else:
                isin = 0
    f.close()
titles.pop(0)
#第二次遍历，写入不同新闻不同时刻的热点
data = [[0] * len(filelist) for i in range(len(titles))]#必须要这样子构建
timeloc = 0
for file in filelist:
    f = open(path+file,'r',newline='',encoding='UTF-8')
    csv_reader = csv.reader(f)
    for row in csv_reader:
        if (row[1]=='热度'):
            continue
        else:
            for i in range(len(titles)):
                if(row[0]==titles[i]):
                    data[i][timeloc] = int(row[1])
                    break
            
    f.close()
    timeloc = timeloc + 1





