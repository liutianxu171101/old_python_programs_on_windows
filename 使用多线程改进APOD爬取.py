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
groups = []

n = 0
while (n*100 < len(son_urls)):
    if ((n+1)*100<len(son_urls)):
        groups.append(son_urls[n*100:(n+1)*100])
    else:
        groups.append(son_urls[n*100:])

    n = n + 1
       
print('已经获取{}个子网页url'.format(len(son_urls)))
print('开始下载')

def download(url):
    res = requests.get(head_url+url,headers = header)
    if(res.status_code != 200):
        return
    else:
        res.encoding = res.apparent_encoding
        img_url = re.findall('<a href="(.*?)">\n<IMG SRC="',res.text)
        if (img_url==[]):
            img_url = re.findall('<a href="(.*?)">\n<img src="',res.text)
        if (img_url == []):
            return

    name = url[:8] + img_url[0][len(img_url[0])-4:len(img_url[0])]
#    num1 = img_url[0].find('/')
#    num2 = img_url[0][num1+1:].find('/')
#    if (num2 == -1):
#        name = img_url[0][num1+1:]
#    else:
#        name = img_url[0][num2+1:]
    urlretrieve(head_url+img_url[0],path+name)
    
if __name__ == '__main__':
    pool = Pool(processes = 8)    
    for i in range(0,len(groups)):
        start1 = time.time()
        if (i<len(groups)-1):
            print(groups[i][0]+'至'+groups[i][99]+'开始下载')
        else:
            print(groups[i][0]+'至'+groups[i][len(groups[i])-1]+'开始下载')
        pool.map(download,groups[i])
        end1 = time.time()
        print('第{}组已经下载完毕，耗时{:.1f}秒'.format(i+1,end1-start1))
        
