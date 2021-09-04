# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 19:59:00 2020

@author: dell
"""

from PIL import Image
img = Image.open('E://刘天旭的资料/XJTUAA/360度全景图/1553418085717.jpeg');

print(img.format)		 # 输出图片基本信息
print(img.mode)
print(img.size)

img2 = img.resize((256,256))

img2 = img2.rotate(45)

img.paste(img2,(300,300))
img.show()
print('森哥挂了')