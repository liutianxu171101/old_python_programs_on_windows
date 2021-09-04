import requests
import re
from urllib.request import urlretrieve
from multiprocessing import Pool
import time

path ='E://Python/mydatas/APOD/'
url_main = 'https://apod.nasa.gov/apod/archivepixFull.html'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
head_url = 'https://apod.nasa.gov/apod/'

res = requests.get(url_main,headers = header)
print('主网页已经打开')
son_urls = re.findall(':  <a href="(.*?)">',res.text)
print('已经获取{}个子网页url'.format(len(son_urls)))
son_urls = son_urls[21:41]
print('开始下载')

def download(url):
    res = requests.get(head_url+url,headers = header)
    if(res.status_code != 200):
        print('网页无法打开')
        return
    else:
        res.encoding = res.apparent_encoding
        jpg_url = re.findall('<a href="(.*?)">\n<IMG SRC="',res.text)
        if (jpg_url==[]):
            jpg_url = re.findall('<a href="(.*?)">\n<img src="',res.text)
        if (jpg_url == []):
            print('{}无法下载'.format(url[:8]))
            return

    name = url[:8]+'.jpg'
    urlretrieve(head_url+jpg_url[0],path+name)
    print('{}已经下载完毕'.format(url[:8]))  
    
if __name__ == '__main__':
    pool = Pool(processes=4)
    pool.map(download,son_urls)
    


