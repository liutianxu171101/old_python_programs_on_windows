#爬取一条信息
import requests
from bs4 import BeautifulSoup

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
    
res = requests.get('http://bj.xiaozhu.com/',headers = header)
soup = BeautifulSoup(res.text,'html.parser')
#page_list > ul > li:nth-of-type(1) > div.result_btm_con.lodgeunitname > span.result_price > i
#price = soup.select('#page_list > ul > li:nth-child(1) > div.result_btm_con.lodgeunitname > div:nth-child(1) > span > i')
price = soup.select('div.result_btm_con.lodgeunitname > div:nth-child(1) > span > i')
print(str(price))
