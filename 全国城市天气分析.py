#月均晴天数、月平均气温、月最高气温、月最低气温、时间序列
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
#--------------------------------------------------------------
class city:
    def init_city(self,name,mon_highest,mon_lowest,mon_average
                  ,mons_highest,mons_lowest,mons_average
                  ,mon_finenight,mon_finenightstd
                  ,year_finenight,year_finenightmean,year_finenightstd):
        self.name = name#城市名称
        self.mon_highest= mon_highest#月最高气温统计平均[12]
        self.mon_lowest = mon_lowest#月最低气温统计平均[12]
        self.mon_average= mon_average#月平均气温统计平均[12]
        self.mons_highest=mons_highest#逐月月最高气温[108]
        self.mons_lowest= mons_lowest#逐月月最低气温[108]
        self.mons_average=mons_average#逐月平均气温[108]
        self.mon_finenight=mon_finenight#每月晴夜数统计平均[12]
        self.mon_finenightstd= mon_finenightstd#每月晴天数标准差[12]
        self.year_finenight=year_finenight#每年的晴夜数[9]
        self.year_finenightmean = year_finenightmean#晴夜均值
        self.year_finenightstd = year_finenightstd#晴夜标准差
        
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
          ,'沈阳','长春','哈尔滨','上海','南京',
          '杭州','合肥','福州','南昌'
          ,'济南','郑州','武汉','长沙','广州'
          ,'南宁','海口','重庆','成都','贵阳'
          ,'昆明','拉萨','西安','兰州','西宁'
          ,'银川','乌鲁木齐','香港','澳门']
years = ['2011','2012','2013','2014','2015','2016','2017','2018','2019']#9
months= ['01','02','03','04','05','06','07','08','09','10','11','12']
path = 'E://Python/mydatas/city_weathers/'

class_city = [];loc = 0
#从csv文件中录入城市信息
#--------------------------------------------------------------
for name in cities:
    df = pd.read_csv(path + name + '.csv')
    df['日期'] = pd.to_datetime(df['日期'])
    df = df.set_index('日期')

    mon_highest = np.zeros(12); mon_lowest = np.zeros(12); mon_average = np.zeros(12); mon_finenightstd = np.zeros(12)
    mons_highest= [];mons_lowest = [];mons_average = []; mons_finenight = [];mon_finenight =np.zeros(12);
    year_finenight = np.zeros(9);
    
    dates = []
    for year in years:
        k = int(year)-2011
        for month in months:
            i = int(month)-1
            date = year + '-' + month
            dates.append(date)
            mons_highest.append(df[date]['最高气温'].max())
            mons_lowest.append(df[date]['最低气温'].min())
            mons_finenight.append(df[date][df[date]['夜晚天气']=='晴']['夜晚天气'].count())
            mons_average.append((0.5*df[date]['最高气温']+0.5*df[date]['最低气温']).mean())
            
            mon_average[i] = mon_average[i]+1/9*(0.5*df[date]['最高气温']+0.5*df[date]['最低气温']).mean()
            mon_finenight[i] = mon_finenight[i] + 1/9*df[date][df[date]['夜晚天气']=='晴']['夜晚天气'].count()
            
        year_finenight[k] = df[year][df[year]['夜晚天气']=='晴']['夜晚天气'].count()

    year_finenightmean = np.mean(year_finenight)
    year_finenightstd = np.std(year_finenight,ddof=1)
    
    for j in range(0,12):
        mon_highest[j]=max(mons_highest[j],mons_highest[j+12],mons_highest[j+24],mons_highest[j+36],mons_highest[j+48]
                           ,mons_highest[j+60],mons_highest[j+72],mons_highest[j+84],mons_highest[j+96])
        mon_lowest[j]=min(mons_lowest[j],mons_lowest[j+12],mons_lowest[j+24],mons_lowest[j+36],mons_lowest[j+48]
                           ,mons_lowest[j+60],mons_lowest[j+72],mons_lowest[j+84],mons_lowest[j+96])
        mon_finenightstd[j]=np.std([mons_finenight[j],mons_finenight[j+12],mons_finenight[j+24],mons_finenight[j+36],mons_finenight[j+48]
                           ,mons_finenight[j+60],mons_finenight[j+72],mons_finenight[j+84],mons_finenight[j+96]],ddof=1)
        
    CITY = city()
    CITY.init_city(cityname[loc],mon_highest,mon_lowest,mon_average
                    ,mons_highest,mons_lowest,mons_average
                    ,mon_finenight,mon_finenightstd
                   ,year_finenight,year_finenightmean,year_finenightstd)
    class_city.append(CITY)
    print('{}城市已经录入完毕'.format(cityname[loc]))
    loc = loc + 1
    
#------------------------------------------------------------------------------------------------
del df,loc,CITY,mon_highest,mon_lowest,mon_average
del mon_finenightstd,mons_highest,mons_lowest,mons_average,mons_finenight,mon_finenight,i,j,k
del cities,cityname,path,year_finenight,year_finenightmean,year_finenightstd
#绘制月晴天数+标准差
#------------------------------------------------------------------------
path = 'E://Python/mydatas/weathers/省会城市每月夜晚晴天数/'
print('绘制月晴天数+标准差')
for city in class_city:
    #使用默认的图窗大小
#    error_params1=dict(elinewidth=1,ecolor='k',capsize=4)#设置误差标记参数
    plt.errorbar(months,city.mon_finenight,yerr=city.mon_finenightstd,capsize=4
                 ,color = 'k',marker = 'o',linewidth = 1)
    plt.ylim(0,32)
    plt.grid()
    plt.title(city.name+'月平均夜晚晴天数')
    plt.xlabel('月份')
    plt.savefig(path+city.name+'.png',dpi=300)
    plt.close()
    print('{}已分析完毕'.format(city.name))

del city,path
#绘制逐月气温数据
#------------------------------------------------------------------------
path = 'E://Python/mydatas/weathers/省会城市气温/'
print('绘制逐月气温数据')
for city in class_city:
    plt.figure(figsize=(15,5))
    plt.plot(dates,city.mons_highest,linestyle = '--',color = 'r',linewidth=0.5,label = '月最高气温')
    plt.plot(dates,city.mons_lowest,linestyle = '--',color = 'b',linewidth=0.5,label = '月最低气温')
    
    plt.plot(dates,city.mons_average,color = 'k',linestyle='-',marker='o',linewidth=1,label = '月平均气温')
    plt.ylim(min(city.mons_lowest)-5,max(city.mons_highest)+15)
    plt.legend(frameon = False,loc = 'upper right')
    plt.xticks(dates[0:108:6],dates[0:108:6],rotation = 45)
    plt.grid()
    plt.title(city.name+'气温')
    plt.savefig(path+city.name+'.png',dpi=300)
    plt.close()
    print('{}已分析完毕'.format(city.name))

del city,path
#绘制月平均气温数据
#---------------------------------------------------------------------------
path = 'E://Python/mydatas/weathers/省会城市月气温/'
print('绘制月平均气温数据')
for city in class_city:
    #使用默认的图窗大小
    plt.plot(months,city.mon_highest,linestyle = 'none',color = 'r',marker = '_',markersize=8,label = '月最高气温')
    plt.plot(months,city.mon_lowest,linestyle = 'none',color = 'b',marker = '_',markersize=8,label = '月最低气温')
    #绘制上下不等的误差线
    a1 = [];a2 = [];a = []
    for i in range(0,12):
        a1.append(city.mon_average[i] - city.mon_lowest[i])
        a2.append(city.mon_highest[i] - city.mon_average[i])
    a = [a1,a2]
    #
    plt.errorbar(months,city.mon_average,yerr=a,color = 'k',marker = 'o',linewidth = 1,label = '月平均气温')
    plt.ylim(min(city.mons_lowest)-10,max(city.mons_highest)+10)
    plt.legend(frameon = False,loc = 'upper right')
    plt.grid()
    plt.title(city.name+'气温')
    plt.xlabel('月份')
    plt.savefig(path+city.name+'.png',dpi=300)
    plt.close()
    print('{}已分析完毕'.format(city.name))

del city,path

#全国城市夜晚晴天数分析
#--------------------------------------------------------
path = 'E://Python/mydatas/weathers/'
table = pd.DataFrame(columns=('城市', '年晴天数均值', '年晴天数标准差'))
for city in class_city:
    table = table.append([{'城市':city.name,'年晴天数均值':city.year_finenightmean,'年晴天数标准差':city.year_finenightstd}], ignore_index=True)

df = table.sort_values(by = '年晴天数均值',ascending = False)
df = df.reset_index(drop = True)
plt.figure(figsize=(12,6))
error_params1=dict(elinewidth=1,ecolor='midnightblue',capsize=2)#设置误差标记参数
plt.ylim(0,250)
plt.bar(df['城市'],df['年晴天数均值'],yerr=df['年晴天数标准差'],error_kw=error_params1,color='slateblue')
for i in range(0,33):
    string = '{:.0f}'.format(df['年晴天数均值'].loc[i])
    if (len(string)==3):
        plt.text(i-0.3,df['年晴天数均值'].loc[i]+3+df['年晴天数标准差'].loc[i],string)
    elif (len(string)==2):
        plt.text(i-0.25,df['年晴天数均值'].loc[i]+3+df['年晴天数标准差'].loc[i],string)
    else:
        plt.text(i-0.15,df['年晴天数均值'].loc[i]+1+df['年晴天数标准差'].loc[i],string)
plt.xticks(df['城市'],df['城市'],rotation = 90)
plt.title('省会城市年均晴天数')
plt.savefig(path+'城市.png',dpi=300)
