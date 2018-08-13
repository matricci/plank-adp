#!/bin/bash 

if [ -e ~/.local/share/plank/themes/Wallpaper ]; then 
	echo "Theme diretory is present"
else 
	mkdir -v ~/.local/share/plank/themes/Wallpaper 
fi
#
# Check depends
if [ -e /usr/bin/python3 ]; then 
	echo "Python3 installed"
else 
	echo "Install Python before try to run again!"
	exit
fi
if [ -e /usr/bin/pip ] ; then 
	echo "Python-pip installed!"
else
	echo "Please install python-pip"
	exit
fi
#
# Install Pillow 
pip install Pillow 
#
# Change the theme to "Wallpaper"
dconf write /net/launchpad/plank/docks/dock1/theme "'Wallpaper'" 


