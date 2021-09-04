# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 11:49:36 2020

@author: dell
"""

import requests
#import time
import tkinter as tk

def spyder():
    res = requests.get(urltext.get())
    res.encoding = res.apparent_encoding
    if (res.status_code == 200):
        var.set("爬取成功")
    else:
        var.set("爬取失败")

window = tk.Tk()
var = tk.StringVar()


text1 = tk.Label(window,text="状态",
                  fg='black')
text2 = tk.Label(window,textvariable=var,
                  fg='red')
text3 = tk.Label(window,text="网址",
                  fg='black')
text1.grid(row=1,column=1,padx=5,pady=5)
text2.grid(row=1,column=2,padx=5,pady=5)
text3.grid(row=2,column=1,padx=5,pady=5)
urltext = tk.Entry()
urltext.grid(row=2,column=2,columnspan=2)
button1 = tk.Button(window,text="爬取网页",command = spyder)
button1.grid(row=3,column=2)

window.mainloop()
