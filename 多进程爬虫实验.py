import requests
import re
import time
import csv
from multiprocessing import Pool

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}



def re_scraper(url):
    f1 = open('db1.csv','w',encoding = 'UTF-8-sig')
    csv_writer = csv.writer(f1)
    res = requests.get(url,headers=header)
    ids = re.findall('<h2>(.*?)</h2>',res.text,re.S)
    contents = re.findall('<div class="content">\n<span>(.*?)</span>'
                          ,res.text,re.S)
    for i in range(len(ids)):
        csv_writer.writerow([ids[i],contents[i]])    
    f1.close()  

if __name__ == '__main__':
    urls = {'http://qiushibaike.com/text/page/{}'.format(str(i)) for i in range(1,14)}
    #    start1 = time.time()
    #    for url in urls:
    #        re_scraper(url)
    #    end1 = time.time()
    #    print('串行爬虫',end1-start1)
    start2 = time.time()
    pool = Pool(processes=4)
    pool.map(re_scraper,urls)
    end2 = time.time()
    print('四进程爬虫',end2-start2)

