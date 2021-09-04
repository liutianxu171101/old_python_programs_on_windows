import requests
import time
import csv
from bs4 import BeautifulSoup


def get_links(url):     #进入详情页
    wb_data = requests.get(url,headers = headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    links= soup.select('#page_list > ul > li > a')
    for link in links:
        href = link.get("href")
        get_info(href)

def get_info(url):
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
        csv_writer.writerow([data['title'],data['address'],data['price'],data['name']])

if __name__ == '__main__':
    
    num = 1;
    f = open('E://Python/mydatas/cs2.csv','w',encoding='UTF-8',newline='')
    csv_writer = csv.writer(f)
    csv_writer.writerow(["title","address","price","name"])
    print('CSV文件创建完毕！')
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'};

    urls = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(num) for num in range(1,14)]
    for single_url in urls:
        get_links(single_url)
        print('----------第%d页浏览完毕----------',%num)
        time.sleep(2)
        num = num + 1

print('CSV文件已关闭')
