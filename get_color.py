#!/usr/bin/python3
# 
from PIL import Image 
import os 
import sys 
import fileinput
#
filename = "wallpaper.jpg"; ## Open image 
image = Image.open( filename ); 
width, height = image.size ## Get image size
# Get 10% of bottom image
num = height * 0.10
num2 = round(num)
num3 = height - num2
dock = int(num3)
#
cropped_image = image.crop( ( 0, dock, width, height ) ); ## Cut the image 
img2 = cropped_image.resize((1, 1),Image.ANTIALIAS) ## Resize to 1x1, same as average 
color = img2.getpixel((0, 0)) ## Get the color
color2=('{};;{};;{};;235'.format(*color)) ## Format the color to replace inside 'dock.theme'
#Here starts the replacement part of the code ;)
f = open('base.theme','r')
filedata = f.read()
f.close()
newdata = filedata.replace("color",color2)
f = open('dock.theme','w')
f.write(newdata)
f.close()