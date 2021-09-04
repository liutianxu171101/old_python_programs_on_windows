import matplotlib.pyplot as plt
import numpy as np
data = np.random.random(30)
fig = plt.figure()
'''【matplotlib.pyplot在图形上显示中文】
plt.rcParams['font.sans-serif']=['STSong']     ## 中文宋体
plt.rcParams['font.sans-serif']=['SimHei']     ## 中文黑体
plt.rcParams['font.sans-serif']=['Kaiti']      ## 中文楷体
plt.rcParams['font.sans-serif']=['Lisu']       ## 中文隶书
plt.rcParams['font.sans-serif']=['FangSong']   ## 中文仿宋
plt.rcParams['font.sans-serif']=['YouYuan']    ## 中文幼圆
【字体粗细、类型 】
styles=['normal','italic','oblique']
weights=['light','normal','medium','semibold','bold','heavy','black']'''
plt.rcParams['font.sans-serif']=['SimHei']     #解决中文显示问题，目前只知道黑体可行
plt.rcParams['axes.unicode_minus']=False       #解决负数坐标显示问题
plt.plot(data)
plt.title('插森')
plt.show()
