#!/usr/bin/python3
# 
from PIL import Image 
import os 
import sys 
import fileinput
#
filename = "wallpaper.jpg";
image = Image.open( filename );
width, height = image.size
num = height * 0.10
num2 = round(num)
num3 = height - num2
dock = int(num3)
print(0, dock, height, width)
cropped_image = image.crop( ( 0, dock, width, height ) );
img2 = cropped_image.resize((1, 1),Image.ANTIALIAS)
color = img2.getpixel((0, 0))
color2=('{};;{};;{};;235'.format(*color))
print(color2)
#Here starts the replacement part of the code ;)
f = open('base.theme','r')
filedata = f.read()
f.close()
newdata = filedata.replace("color",color2)
f = open('dock.theme','w')
f.write(newdata)
f.close()