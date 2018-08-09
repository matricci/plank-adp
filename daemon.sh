	#!/bin/bash
# 
#
while : ; do 
	if [ "$XDG_CURRENT_DESKTOP" = "MATE" ] ; then
	sleep 0.5s
	name=$(dconf read /org/mate/desktop/background/picture-filename | tr -d \')
	sleep 0.5s
fi 
	if [ "$XDG_CURRENT_DESKTOP" = "ubuntu:GNOME" ] ; then 
	sleep 0.5
	name=$(dconf read /org/gnome/desktop/background/picture-uri | tr -d \' | cut -c 8-)
	sleep 0.5
fi
	if [ "$XDG_CURRENT_DESKTOP" = "GNOME" ] ; then 
	sleep 0.5
	name=$(dconf read /org/gnome/desktop/background/picture-uri | tr -d \' | cut -c 8-)
	sleep 0.5
fi
if [ "$XDG_CURRENT_DESKTOP" = "X-Cinnamon" ]; then
	name=$(dconf read /org/cinnamon/desktop/background/picture-uri | tr -d \' | cut -c 8-)
fi
sleep 0.3s
	if [ "$(cat $name | md5sum)" != "$(cat wallpaper.jpg | md5sum)" ]; then
	bash main.sh
fi	
sleep 6s
done	
