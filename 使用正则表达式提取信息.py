import requests
import re
import time

res = requests.get('http://www.doupoxs.com/doupocangqiong/1.html',headers = header)
prices = re.findall('<p>(.*?)</p>',res.content.decode('utf-8'),re.S)
for price in prices:
    print(price)

print('运行结束\n')
