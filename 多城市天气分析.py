#月均晴天数、月平均气温、月最高气温、月最低气温、时间序列
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

class city:
    
    def init_city(self,name,mon_highest,mon_lowest,mon_average
                  ,mons_highest,mons_lowest,mons_average
                  ,mon_finenight):
        self.name = name#城市名称
        self.mon_highest= mon_highest#月最高气温统计平均[12]
        self.mon_lowest = mon_lowest#月最低气温统计平均[12]
        self.mon_average= mon_average#月平均气温统计平均[12]
        self.mons_highest=mons_highest#逐月月最高气温[108]
        self.mons_lowest= mons_lowest#逐月月最低气温[108]
        self.mons_average=mons_average#逐月平均气温[108]
        self.mon_finenight=mon_finenight#每月晴夜数统计平均[12]
        

plt.rcParams['font.sans-serif']=['SimHei']     #解决中文显示问题，目前只知道黑体可行
plt.rcParams['axes.unicode_minus']=False       #解决负数坐标显示问题
#日期,白天天气,夜晚天气,最高气温,最低气温
cities = ['beijing','tianjin','shijiazhuang','taiyuan'
              ,'huhehaote','shenyang','changchun','haerbin'
              ,'shanghai','nanjing','hangzhou','hefei'
              ,'fujianfuzhou','nanchang','jinan','zhengzhou'
              ,'wuhan','changsha','guangzhou','nanning'
              ,'haikou','chongqing','chengdu','guiyang'
              ,'kunming','lasa','xian','lanzhou'
              ,'xining','yinchuan','wulumuqi'
              ,'xianggang','aomen']
cityname=['北京','天津','石家庄','太原','呼和浩特'
          ,'沈阳','长春','哈尔滨','福州','南昌'
          ,'济南','郑州','武汉','长沙','广州'
          ,'南宁','海口','重庆','成都','贵阳'
          ,'昆明','拉萨','西安','兰州','西宁'
          ,'银川','乌鲁木齐','香港','澳门']
years = ['2011','2012','2013','2014','2015','2016','2017','2018','2019']#9
months= ['01','02','03','04','05','06','07','08','09','10','11','12']
path = 'E://Python/mydatas/city_weathers/'

class_city = [];loc = 0
for name in cities:
    df = pd.read_csv(path + name + '.csv')
    df['日期'] = pd.to_datetime(df['日期'])
    df = df.set_index('日期')

    mon_highest = np.zeros(12); mon_lowest = np.zeros(12); mon_average = np.zeros(12);
    mons_highest= [];mons_lowest = [];mons_average = [];
    mon_finenight=np.zeros(12);

    for year in years:
        for month in months:
            i = int(month)-1
            date = year + '-' + month
            mons_highest.append(df[date]['最高气温'].max())
            mons_lowest.append(df[date]['最低气温'].min())
            mons_average.append((0.5*df[date]['最高气温']+0.5*df[date]['最低气温']).mean())
            mon_highest[i] = mon_highest[i]+1/9*df[date]['最高气温'].max()
            mon_lowest[i] = mon_lowest[i]+1/9*df[date]['最低气温'].min()
            mon_average[i] = mon_average[i]+1/9*(0.5*df[date]['最高气温']+0.5*df[date]['最低气温']).mean()
            mon_finenight[i] = mon_finenight[i] + 1/9*df[date][df[date]['夜晚天气']=='晴']['夜晚天气'].count()

    CITY = city()
    CITY.init_city(cityname[loc],mon_highest,mon_lowest,mon_average
                    ,mons_highest,mons_lowest,mons_average
                    ,mon_finenight)
    class_city.append(CITY)
    print('{}城市已经录入完毕'.format(cityname[loc]))
    loc = loc + 1
