import requests
import re
from urllib.request import urlretrieve
import time

path ='E://Python/mydatas/APOD2/'
url_main = 'https://apod.nasa.gov/apod/archivepix.html'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
head_url = 'https://apod.nasa.gov/apod/'
success_num,fail_num = 0,0

res = requests.get(url_main,headers = header)
print('主网页已经打开')
son_urls = re.findall(':  <a href="(.*?)">',res.text)
titles = re.findall('">(.*?)</a><br>',res.text)
print('已经获取{}个子网页url'.format(len(son_urls)))
print('开始下载')

start_time = time.time()

for i in range(879,1000):
    res = requests.get(head_url+son_urls[i],headers = header)
    if(res.status_code != 200):
        continue
        print('网页无法打开')
    else:
        res.encoding = res.apparent_encoding
        jpg_url = re.findall('<a href="(.*?)">\n<IMG SRC="',res.text)
        if (jpg_url==[]):
            jpg_url = re.findall('<a href="(.*?)">\n<img src="',res.text)
        if (jpg_url == []):
            print('第{}张 {}无法下载'.format(i+1,titles[i]))
            fail_num = fail_num + 1;
            continue
    
    name = titles[i]+'.jpg'
    urlretrieve(head_url+jpg_url[0],path+name)
    print('第{}张 {}已经下载完毕'.format(i+1,titles[i]))
    success_num = success_num + 1

end_time = time.time()
print('下载成功{}张，下载失败{}张，耗时{}'.format(success_num,fail_num,end_time-start_time))
