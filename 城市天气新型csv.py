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

    del dates[0]
    del weads[0]
    del temps[0]
    for i in range(len(dates)):
            da = re.sub('[\n\r ]','',dates[i].get_text().strip()) #日期
            da.replace('年','-').replace('月','-').replace('日','')#2019-7-21
            ww = re.sub('[\n\r ]','',weads[i].get_text().strip())#白天天气/夜晚天气
            wwd,wwn = ww.split('/')                             #白天天气、夜晚天气
            te = re.sub('[\n\r ]','',temps[i].get_text().strip())
            teh,tel = te.split('/') 

            DA = da.replace('年','-').replace('月','-').replace('日','')
    
            csv_writer.writerow([DA,wwd,wwn,teh.replace('℃',''),tel.replace('℃','')])
    

if __name__ == '__main__':
    cities = ['beijing','tianjin','shijiazhuang','taiyuan'
              ,'huhehaote','shenyang','changchun','haerbin'
              ,'shanghai','nanjing','hangzhou','hefei'
              ,'fujianfuzhou','nanchang','jinan','zhengzhou'
              ,'wuhan','changsha','guangzhou','nanning'
              ,'haikou','chongqing','chengdu','guiyang'
              ,'kunming','lasa','xian','lanzhou'
              ,'xining','yinchuan','wulumuqi','taibei'
              ,'xianggang','aomen']
    
    for i in range(len(cities)):
        city = cities[i]
        f = open('E://Python/mydatas/weathers/'+city + '.csv','w',encoding='UTF-8',newline='')
        csv_writer = csv.writer(f)
        csv_writer.writerow(["日期","白天天气","夜晚天气","最高气温","最低气温"])
        head_url = 'http://www.tianqihoubao.com/lishi/'+ city + '/month/'
        print('开始解析')
        for year in range(2011,2020):
            sta = time.time()
            for month in range(1,13):
                if month < 10:
                    part = str(year)+'0'+str(month)+'.html'
                else:
                    part = str(year)+str(month)+'.html'
                    
                getinformation(head_url+part)
            end = time.time()    
            print('{}已经解析完毕\t耗时{:.1f}秒'.format(city+str(year),end-sta))
            
        f.close()    
    
        
