import requests
import json
import pprint

add = '辽宁省沈阳市沈阳故宫'
head_url = 'http://api.map.baidu.com/geocoding/v3/?address='
key = 'I1RYILrzGzZ1V3QOcBm7v7n9mMkq85dP'
#ret_coordtype地理坐标编码，缺省为百度编码
url = head_url+add+'&output=json&ak='+key+'&ret_coordtype=bd09ll'
res = requests.get(url)
json_data = json.loads(res.text)
loc = json_data['result']['location']
print(loc['lng'],loc['lat'])
