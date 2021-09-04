import requests
import re

urls = []
head_url = 'https://www.changhai.org/articles/science/astronomy/sun/'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}


for i in range(1,2):
    if (i<10):
        urls.append(head_url+'0'+str(i)+'.php')
    else:
        urls.append(head_url+str(i)+'.php')

loc = 1
for url in urls:
    res = requests.get(url,headers = header)
    res.encoding = 'utf-8'
    contents = re.findall('<p>(.*?)</p>',res.text)
    for content in contents:
        print('{}\n'.content)

    print('第{}章爬取完毕'.format(loc))
    loc = loc + 1    
