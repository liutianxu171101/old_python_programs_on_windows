# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 10:55:53 2020

@author: dell
"""
import requests
import re
import time
import csv

num = 0
while(num<100):
    time_now = time.ctime()
    time_now = time_now.replace(':',' ')
    minute = int(time_now[14:16])
    if(minute%3==0): 
        num = num + 1
        res = requests.get('http://top.baidu.com/')
        res.encoding = res.apparent_encoding
        print(time_now)
        time.sleep(5)
        titles = re.findall('title="(.*?)" data="',res.text);
        titles = titles[0:20]
        hotpoint = re.findall('<span class="icon-rise">(.*?)</span>',res.text)
        hotpoint = hotpoint[0:20]
        
        f = open('E://Python/programs/热榜/' + time_now + '.csv','w',encoding='UTF-8',newline='')
        csv_writer = csv.writer(f)
        csv_writer.writerow(['标题','热度'])
        for i in range (1,20):
            csv_writer.writerow([titles[i],hotpoint[i]])
                
        f.close()
    time.sleep(55)
print('森哥挂了')