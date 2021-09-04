# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 20:56:59 2020

@author: dell
"""

import requests
import re
import tkinter as tk

def spyder():
    global array1
    res = requests.get(urltext.get())
    res.encoding = res.apparent_encoding
    if (res.status_code == 200):
        var_status.set("爬取成功")
    else:
        var_status.set("爬取失败")
    print(res.text)
    array1 = re.findall(fronttext.get()+'(.?*)'+behindtext.get(),res.text)

window = tk.Tk()
window.title('使用正则表达式爬取信息')
var_status = tk.StringVar()


text1 = tk.Label(window,text="状态",fg='black')
text2 = tk.Label(window,textvariable=var_status,fg='red')
text3 = tk.Label(window,text="网址",fg='black')
text4 = tk.Label(window,text="前缀")
text5 = tk.Label(window,text="后缀")
text1.grid(row=1,column=1,padx=5,pady=5)#状态提示
text2.grid(row=1,column=2,padx=5,pady=5)#连接状态
text3.grid(row=2,column=1,padx=5,pady=5)#网址提示
text4.grid(row=3,column=1,padx=5,pady=5)#前缀提示
text5.grid(row=4,column=1,padx=5,pady=5)#后缀提示

urltext = tk.Entry()#输入网址
urltext.grid(row=2,column=2)
fronttext = tk.Entry()#输入前缀
fronttext.grid(row=3,column=2)
behindtext = tk.Entry()#输入后缀
behindtext.grid(row=4,column=2)
button1 = tk.Button(window,text="爬取网页",command = spyder)
button1.grid(row=5,column=2)

window.mainloop()
