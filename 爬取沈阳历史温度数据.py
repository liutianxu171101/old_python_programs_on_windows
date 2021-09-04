import requests
from bs4 import BeautifulSoup
import csv
import re
import time
#content > table > tbody > tr:nth-child(2) > td:nth-child(1)
#content > table > tbody > tr:nth-child(2) > td:nth-child(2)
#content > table > tbody > tr:nth-child(2) > td:nth-child(3)


def getinformation(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'lxml')
    dates = soup.select('tr > td:nth-child(1)')
    weads = soup.select('tr > td:nth-child(2)')
    temps = soup.select('tr > td:nth-child(3)')
    winds = soup.select('tr > td:nth-child(4)')
    del dates[0]
    del weads[0]
    del temps[0]
    del winds[0]
    for i in range(len(dates)):
        DA = re.sub('[\n\r ]','',dates[i].get_text().strip())
        WW = re.sub('[\n\r ]','',weads[i].get_text().strip())
        TE = re.sub('[\n\r ]','',temps[i].get_text().strip())
        WI = re.sub('[\n\r ]','',winds[i].get_text().strip())
        csv_writer.writerow([DA,WW,TE,WI])
    

if __name__ == '__main__':

    f = open('hangzhou.csv','w',encoding='UTF-8',newline='')
    csv_writer = csv.writer(f)
    csv_writer.writerow(["日期","天气","气温","风力"])
    head_url = 'http://www.tianqihoubao.com/lishi/hangzhou/month/'
    sta = time.time()
    for year in range(2011,2020):
        for month in range(1,13):
            if month < 10:
                part = str(year)+'0'+str(month)+'.html'
            else:
                part = str(year)+str(month)+'.html'
                
            getinformation(head_url+part)
            print('{}解析完毕'.format(part))
    end = time.time()
    print('共用时{}秒'.format(end-sta))
    f.close()
