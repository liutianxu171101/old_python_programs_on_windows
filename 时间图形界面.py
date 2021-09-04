# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 11:27:39 2020

@author: dell
"""

import tkinter as tk
import time

window = tk.Tk()
var = tk.StringVar()

window.title('浮动窗口')
label1 = tk.Label(window,textvariable=var,
                  fg='red',font=("Times New Roman",80))
label1.pack()
def gettime():
    var.set(time.ctime())
    window.after(500,gettime)
label1.after(500,gettime)

window.mainloop()
