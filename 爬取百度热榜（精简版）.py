# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 16:18:42 2020

@author: dell
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 10:55:53 2020

@author: dell
"""
from requests import get
from re import findall
from time import ctime
from time import sleep
import csv

numbers = int(input('请输入爬取总次数：'))
t = 15
while(True):
    t = int(input('输入爬取时间间隔(min)：'))
    if (t>10)|(t==1):
        print('时间不合适，重新输入，2-10min')
    else:
        break
print('===开始===')
num = 0
while(num<numbers):
    time_now = ctime()
    
    minute = int(time_now[14:16])
    if(minute%t==0): 
        num = num + 1
        res = get('http://top.baidu.com/')
        res.encoding = res.apparent_encoding
        print('第' + str(num) + '次爬取，时间' + time_now)
        sleep(5)
        titles = findall('title="(.*?)" data="',res.text);
        titles = titles[0:20]
        hotpoint = findall('<span class="icon-rise">(.*?)</span>',res.text)
        hotpoint = hotpoint[0:20]
        time_now = time_now.replace(':',' ')
        f = open('E://Python/programs/热榜/' + time_now + '.csv','w',encoding='UTF-8',newline='')
        csv_writer = csv.writer(f)
        csv_writer.writerow(['标题','热度'])
        for i in range (20):
            csv_writer.writerow([titles[i],hotpoint[i]])
                
        f.close()
        print('写入完成，进度' + str((num)/numbers*100)+'%')
    sleep(55)
print('森哥挂了')