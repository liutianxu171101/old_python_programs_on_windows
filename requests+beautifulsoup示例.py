# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 22:02:15 2020

@author: dell
"""

import requests
from bs4 import BeautifulSoup

useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
cookie = 'BAIDUID=59D311DA6F330B370B1B48702F27D231:FG=1; PSTM=1585554342; BIDUPSID=5CE38F4C0F18027AF57EAED712B55E1B; BDUSS=jRlcFk5SGlVTzFPSTR0dlBkeHMtU35OWWZNaWhSdWs5cDJpZGpVbmxHd2dQcWxlRVFBQUFBJCQAAAAAAAAAAAEAAAAlKay1bGl1dGlhbnh1OTgwOQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCxgV4gsYFeT; BDUSS_BFESS=jRlcFk5SGlVTzFPSTR0dlBkeHMtU35OWWZNaWhSdWs5cDJpZGpVbmxHd2dQcWxlRVFBQUFBJCQAAAAAAAAAAAEAAAAlKay1bGl1dGlhbnh1OTgwOQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCxgV4gsYFeT; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=1; H_PS_PSSID=32809_32617_1430_32735_31660_32723_32230_7517_32117_32718_26350'
header = {'User-Agent':useragent,
           'cookie':cookie}
url = "http://www.shanghairanking.cn/rankings/bcur/2020"
res = requests.get(url,headers=header)
res.raise_for_status()
res.encoding = res.apparent_encoding
soup = BeautifulSoup(res.text,"html.parser")

name = soup.select('tbody > tr > td.align-left > a')
score= soup.select('tbody > tr > td:nth-child(5)')
num = 20
for i in range(20):
    print(name[i].get_text()+'\t'+score[i].get_text())
    
#content-box > div.rk-table-box > table > tbody > tr:nth-child(2) > td:nth-child(1)
#content-box > div.rk-table-box > table > tbody > tr:nth-child(2) > td.align-left > a
#content-box > div.rk-table-box > table > tbody > tr:nth-child(2) > td:nth-child(3)
#content-box > div.rk-table-box > table > tbody > tr:nth-child(2) > td:nth-child(4)
#content-box > div.rk-table-box > table > tbody > tr:nth-child(2) > td:nth-child(5)
#content-box > div.rk-table-box > table > tbody > tr:nth-child(2) > td:nth-child(6)
