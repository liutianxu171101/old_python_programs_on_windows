import requests
import json
import re
import csv

if __name__ == '__main__':
    head_url = 'http://api.map.baidu.com/geocoding/v3/?address='
    key = 'I1RYILrzGzZ1V3QOcBm7v7n9mMkq85dP'
    #ret_coordtype地理坐标编码，缺省为百度编码
    f = open('房价+坐标3.csv','w',encoding='UTF-8',newline='')
    csv_writer = csv.writer(f)
    csv_writer.writerow(["名称","地址","价格","经度","纬度"])
    depth = 14
    main_urls = ['http://sy.xiaozhu.com/search-duanzufang-p{}-0/'.format(num) for num in range(1,depth)]
    for i in range(1,depth):
        a = list(["名称","地址","价格","经度","纬度"])
        res = requests.get(main_urls[i])
        my_urls = re.findall('detailurl="(.*?)" style="',res.text)
        titles = re.findall('<span class="result_title hiddenTxt">(.*?)</span>',res.text)
        for i in range(0,len(titles)):
            a[0] = titles[i]
            res2 = requests.get(my_urls[i])
            addres = re.findall('<span class="pr5">(.*?)\n',res2.text)
            prices = re.findall('<span class="detail_avgprice">(.*?)</span><em>',res2.text)
            a[1] = addres[0]
            a[2] = prices[0]

            baiduurl = head_url+addres[0]+'&output=json&ak='+key+'&ret_coordtype=bd09ll'
            baidures = requests.get(baiduurl)
            json_data = json.loads(baidures.text)
            loc = json_data['result']['location']
            a[3] = loc['lng']
            a[4] = loc['lat']
            csv_writer.writerow(a)
        print('第{}页解析完毕'.format(i))

    f.close()
