# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 10:22:44 2020

@author: dell
"""

import tkinter as tk
window = tk.Tk()    #创建窗口
window.minsize(600,300) #窗口的大小
window.title('插森窗口')
var = tk.StringVar()

label1 = tk.Label(window,textvariable=var,
                  fg='red')
var.set("开始插森吧")
label1.grid(row=1,column=1)

def insertsen():
    var.set("森哥挂了")
   
def reinsertsen():
    var.set("开始插森吧")

button1 = tk.Button(text="插森",command=insertsen)
button1.grid(row=2,column=1)

button2 = tk.Button(text="重新开始",command=reinsertsen)
button2.grid(row=2,column=2)

window.mainloop()
