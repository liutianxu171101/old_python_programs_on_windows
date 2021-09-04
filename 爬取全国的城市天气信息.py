import requests
from bs4 import BeautifulSoup
import re
import time

def getinformation(url):
    DA = [];WWD = [];WWN = [];TEH = [];TEL = []
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'lxml')
    dates = soup.select('tr > td:nth-child(1)')#bs4格式的数据
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
        teh,tel = te.split('/')                             #最高气温，最低气温
        teh.replace('℃','');tel.replace('℃','')
        DA.append(da.replace('年','-').replace('月','-').replace('日',''))
        WWD.append(wwd);WWN.append(wwn)
        TEH.append(int(teh.replace('℃','')))
        TEL.append(int(tel.replace('℃','')))
        
    return DA,WWD,WWN,TEH,TEL


if __name__ == '__main__':
    city = 'shenyang'
    f1 = open('dates_{}.csv'.format(city),'w',encoding = 'utf-8',newline = '')
    csv_writer1 = csv.writer(f1)
#    DA_ALL = [];WWD_ALL = [];WWN_ALL = [];TEH_ALL = [];TEL_ALL = []
    head_url = 'http://www.tianqihoubao.com/lishi/xian/month/'
    sta = time.time()
    for year in range(2011,2013):
        for month in range(1,13):
            if month < 10:
                part = str(year)+'0'+str(month)
            else:
                part = str(year)+str(month)

            
                
            DA,WWD,WWN,TEH,TEL = getinformation(head_url+part+'.html')

#            DA_ALL.append(DA)
#            WWD_ALL.append(WWD)
#            WWN_ALL.append(WWN)
#            TEH_ALL.append(TEH)
#            TEL_ALL.append(TEL)
            print('{}解析完毕'.format(part))
            
    end = time.time()
    print('共用时{}秒'.format(end-sta))
