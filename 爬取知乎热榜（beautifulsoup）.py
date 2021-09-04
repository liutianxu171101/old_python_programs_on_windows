# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 20:20:17 2020

@author: dell
"""

import requests
from bs4 import BeautifulSoup
import time
import csv

url = 'https://www.zhihu.com/hot'
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
cookie = '_zap=bd793d3c-16c9-402a-a0d1-3e27989c3f19; d_c0="ALCXIkWUEhGPTuYKAtvzc8mhXGC7QWQDulg=|1586084603"; _ga=GA1.2.2009306571.1586084608; _xsrf=spdeeCLdqbRpBNUAHkmXsuCuuqKtZlEz; z_c0="2|1:0|10:1596538289|4:z_c0|92:Mi4xbVlSaEVRQUFBQUFBc0pjaVJaUVNFU1lBQUFCZ0FsVk5zWXNXWUFBZW5Zc2FsZ2lEZ01CY21ua0dPbUZHSFBsLTd3|a17a4ea85aca6f2f5d7f124bfa87087aaa9a37a5e1fed5186afb362c026de0c9"; tshl=; _gid=GA1.2.1665349097.1601655444; q_c1=f630ea8e1c7a49d58b8494934fd13a66|1601655591000|1597723629000; tst=h; SESSIONID=uF5gufGT7bzxtgQaQyIBl6H2AXQbbRenS9IkOGxOOyk; JOID=V1wdAkrLgwQ-mwoWDs-2X2eS0FsSv8k4WeptXVP44HJP72lGY_G3dGWeBxMH2OkY0wRF2VXySBkJNvbKGsmZNzM=; osd=U1oRCk3PhQg2nA4QAsexW2Ge2FwWucUwXu5rUVv_5HRD525CZf2_c2GYCxsA3O8U2wNB31n6Tx0POv7NHs-VPzQ=; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1601655443,1601729602,1601777670,1601778448; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1601778464; KLBRSID=e42bab774ac0012482937540873c03cf|1601778464|1601777670'
header = {'User-Agent':useragent,'cookie':cookie}

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
    time_now = time.ctime()
    
    minute = int(time_now[14:16])
    if(minute%t==0): 
        num = num + 1
        res = requests.get(url,headers=header)
        print('第' + str(num) + '次爬取，时间' + time_now)
        time.sleep(5)
        res.encoding = res.apparent_encoding
        soup=BeautifulSoup(res.text,'html.parser')
        titles = soup.select('div.HotList-list > section > div.HotItem-content > a > h2')
        time_now = time_now.replace(':',' ')
        hotpoints= soup.select('div.HotList-list > section > div.HotItem-content > div')
        f = open('E://Python/programs/热榜2/' + time_now + '.csv','w',encoding='UTF-8',newline='')
        csv_writer = csv.writer(f)
        csv_writer.writerow(['标题','热度'])
        
        for i in range (20):
            csv_writer.writerow([titles[i].get_text(),hotpoints[i].get_text()])
                
        f.close()
        print('写入完成，进度' + str((num)/numbers*100)+'%')
    time.sleep(55)
print('森哥挂了')
        
