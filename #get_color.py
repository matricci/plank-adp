import os 
import sys 
import fileinput
f = open('dock.theme','r')
filedata = f.read()
f.close()

newdata = filedata.replace("color","another_color")

f = open('fileout','w')
f.write(newdata)
f.close()