import requests
import csv
from bs4 import BeautifulSoup

url = 'http://bj.xiaozhu.com/fangzi/134966002303.html'
f = open('E://Python/mydatas/cs2.csv','w',encoding='UTF-8',newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(["title","address","price","name"])

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
wb_data = requests.get(url,headers = headers)
soup = BeautifulSoup(wb_data.text,'lxml')
titles = soup.select('div.pho_info > h4')
addresses= soup.select('span.pr5')
prices = soup.select('#pricePart > div.day_l > span')
names = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')

for title,address,price,name in zip(titles,addresses,prices,names):
    data = {
            'title':title.get_text().strip(),
            'address':address.get_text().strip(),
            'price':price.get_text(),
            'name':name.get_text()}
    print(data)
csv_writer.writerow([data['title'],data['address'],data['price'],data['name']])
    

f.close()
