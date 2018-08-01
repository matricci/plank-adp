#!/bin/bash 
name=$(dconf read /org/mate/desktop/background/picture-filename | tr -d \') ## For MATE Desktop
#name=$(dconf read /org/gnome/desktop/background/picture-uri | tr -d \' | cut -c 8-) ## For Gnome Destop 
cp -v $name $PWD/wallpaper.jpg
python test1.py 
sudo cp -v dock.theme /usr/share/plank/themes/Wallpaper/
