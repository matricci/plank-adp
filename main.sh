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
if [ "$XDG_CURRENT_DESKTOP" = "GNOME" ] ; then 
	sleep 0.5
	name=$(dconf read /org/gnome/desktop/background/picture-uri | tr -d \' | cut -c 8-)
	sleep 0.5
fi

cp $name $PWD/wallpaper.jpg
python get_color.py 
cp dock.theme ~/.local/share/plank/themes/Wallpaper/
echo $name > .name.config