import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve


download_links = []
path ='E://Python/mydatas/'
url = 'http://mzitu.com/'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}

res = requests.get(url,headers = header)
soup = BeautifulSoup(res.text,'lxml')
imgs = soup.select('li > a > img')
for img in imgs:
    print(img.get('data-original'))
    download_links.append(img.get('data-original'))

for item in download_links:
    urlretrieve(item,path+item[-10:])
