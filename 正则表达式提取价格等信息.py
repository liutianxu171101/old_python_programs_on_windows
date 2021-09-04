import requests
import re
import time

header ={
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': '_uab_collina=157918588095985489117275; _pykey_=14cd32eb-0185-55b8-9e22-fb62f9e17558; gr_user_id=f74b71b0-a24c-469b-a7ee-e3046ccfbe0b; 59a81cc7d8c04307ba183d331c373ef6_gr_last_sent_cs1=N%2FA; grwng_uid=caba6d58-06e1-4797-b32c-2f4861821b2a; abtest_ABTest4SearchDate=b; TY_SESSION_ID=276154c3-a6fa-4362-a06b-a896a9f87988; Hm_lvt_92e8bc890f374994dd570aa15afc99e1=1579187697,1579187882,1579758778,1579856591; Hm_lpvt_92e8bc890f374994dd570aa15afc99e1=1579856591',
'Host': 'bj.xiaozhu.com',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}

res = requests.get('http://bj.xiaozhu.com/',headers = header)
time.sleep(3)
prices = re.findall('<span class="result_price">&#165;<i>(.*?)</i>',res.text)
titles = re.findall('<span class="result_title hiddenTxt">(.*?)</span>',res.text)
for i in range(1,len(prices)):
    print(titles[i]+'\n'+prices[i])

print('共抓{}个数据，运行结束\n'.format(len(prices)))
