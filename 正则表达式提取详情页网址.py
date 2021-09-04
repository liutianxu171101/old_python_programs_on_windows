import requests
import re
import time
import csv

#APOD网址：https://apod.nasa.gov/apod/archivepixFull.html
#两个特例的日期：September 20 1996           2007 July 16
header ={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}

res = requests.get('https://apod.nasa.gov/apod/archivepixFull.html',headers = header)
time.sleep(3)
if(res.status_code==200):
    print('网页打开成功')
res.encoding = res.apparent_encoding
print('网页代码格式转换成功')

dates = re.findall('\n{1,2}(.*?):  <a',res.text)
htmls = re.findall(':  <a href="(.*?)">',res.text)
titles= re.findall('.html">(.*?)</a>\n{0,1}<br>',res.text)
print('信息爬取成功')
'''
fp = open('APOD网页信息2.csv','w',encoding='UTF-8',newline='')
csv_writer = csv.writer(fp)
head = 'https://apod.nasa.gov/apod/'
print('CSV文件创建成功')

csv_writer.writerow(["序号","日期","标题","网址"])

for i in range(0,len(dates)):
    csv_writer.writerow([str(i+1),dates[i],titles[i],head+htmls[i]])
    
print('CSV书写成功')
fp.close()
print('文件已关闭')'''
