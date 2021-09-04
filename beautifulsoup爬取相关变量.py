# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 09:42:51 2020

@author: dell
"""

import requests
from bs4 import BeautifulSoup
import sys

Arrays = []#数据集
infos = []#关联信息集

num = 1

url = input("请输入网址：")
useragent = input('请输入user-agent，输入Y选择默认：')
if useragent == 'Y':
    useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
cookie = input('请输入cookie，输入Y选择默认：')
if cookie == 'Y':
    cookie = 'BAIDUID=59D311DA6F330B370B1B48702F27D231:FG=1; PSTM=1585554342; BIDUPSID=5CE38F4C0F18027AF57EAED712B55E1B; BDUSS=jRlcFk5SGlVTzFPSTR0dlBkeHMtU35OWWZNaWhSdWs5cDJpZGpVbmxHd2dQcWxlRVFBQUFBJCQAAAAAAAAAAAEAAAAlKay1bGl1dGlhbnh1OTgwOQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCxgV4gsYFeT; BDUSS_BFESS=jRlcFk5SGlVTzFPSTR0dlBkeHMtU35OWWZNaWhSdWs5cDJpZGpVbmxHd2dQcWxlRVFBQUFBJCQAAAAAAAAAAAEAAAAlKay1bGl1dGlhbnh1OTgwOQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCxgV4gsYFeT; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=1; H_PS_PSSID=32809_32617_1430_32735_31660_32723_32230_7517_32117_32718_26350'
header = {'User-Agent':useragent,
           'cookie':cookie}
res = requests.get(url,headers=header)
res.encoding = res.apparent_encoding
soup = BeautifulSoup(res.text,'lxml')

if res.status_code == 200:
    print('===爬取成功===')
else:
    sys.exit()

while(1):
    info = input('请输入变量'+str(num)+'的关联信息：')
    infos.append(info)

    yn = input('是否停止爬取(Y/N)：')
    if yn == 'Y':
        break
    else:
        num = num + 1
    
for i in range(0,num):
    Arrays.append(soup.select(info[i]))

print('===解析完成===')

for i in range(0,num):
    print('变量'+str(i)+'的长度为'+str(len(Arrays[i])))
print('=========')
#输出前几位
for i in range(0,3):
    print(Arrays[0][i],Arrays[1][i])
yn = input('是否数据截取(Y/N)：')
if yn == 'Y':
    length = int(input('请输入保留数据长度:'))
    for i in range(0,num):
        Arrays[i] = Arrays[i][0:length]
    print('===数据截断已完成===')
