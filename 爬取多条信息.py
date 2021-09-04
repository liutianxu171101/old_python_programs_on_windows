#爬取多条信息
import requests
from bs4 import BeautifulSoup
#import csv

#fp = open('插森2.csv','w',encoding='UTF-8',newline='')
#writer = csv.writer(fp)
#writer.writerow(["price"])
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
res = requests.get('http://bj.xiaozhu.com/',headers = header)
soup = BeautifulSoup(res.text,'html.parser')

prices = soup.select('#page_list > ul > li > div.result_btm_con.lodgeunitname > div > span > i')
for price in prices:
    print(price.get_text())
#    writer.writerow([str(price.get_text())])

#fp.close()
