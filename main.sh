#!/bin/bash
#
#
if [ "$XDG_CURRENT_DESKTOP" = "MATE" ] ; then
	name=$(dconf read /org/mate/desktop/background/picture-filename | tr -d \')
fi 
if [ "$XDG_CURRENT_DESKTOP" = "ubuntu:GNOME" ] ; then 
	name=$(dconf read /org/gnome/desktop/background/picture-uri | tr -d \' | cut -c 8-)
fi 
if [ "$XDG_CURRENT_DESKTOP" = "X-Cinnamon" ]; then
	name=$(dconf read /org/cinnamon/desktop/background/picture-uri | tr -d \' | cut -c 8-)
fi	
cp -v $name $PWD/wallpaper.jpg
python get_color.py 
cp -v dock.theme ~/.local/share/plank/themes/Wallpaper/
echo $name > .name.config