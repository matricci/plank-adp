#!/bin/bash 

if [ -e ~/.local/share/plank/themes/Wallpaper ]; then 
	echo "Theme diretory is present"
else 
	mkdir -v ~/.local/share/plank/themes/Wallpaper 
fi
#
# Check depends
if [ -e /usr/bin/python3 ]; then 
	echo "Python installed"
else 
	echo "Install Python before try to run again!"
	exit
fi
if [ -e /usr/bin/pip3 ] ; then 
	echo "Python-pip installed!"
else
	echo "Please install python-pip"
	exit
fi

if [ -e /usr/bin/dconf ] ; then
	echo "Dconf-tools installed!"
else
	echo "Please install dconf-tools"
	exit
fi
# 
# 
# Install Packages
pip3 install Pillow 
pip3 install pycairo
pip3 install PyGobject

#
path="/usr/share/plank-adp"
sudo mkdir -v $path
sudo mkdir -v $path/ui
sudo mkdir -v $path/bin
sudo cp -v ../ui/form1.glade $path/ui 
sudo cp -v ../src/form1.py $path/bin
sudo cp -v ../base.theme $path
sudo cp -v plank-adp /usr/bin/
sudo cp -v ../src/plank-adp.desktop /usr/share/applications/
sudo cp -v ../ui/plank-adp.svg /usr/share/icons/hicolor/128x128/apps
sudo chmod a=+rwx $path
sudo chmod 0655 /usr/share/icons/hicolor/128x128/apps/plank-adp.svg

# Change the theme to "Wallpaper"
dconf write /net/launchpad/plank/docks/dock1/theme "'Wallpaper'"

# post-install 
sudo update-desktop-database /usr/share/applications/
sudo gtk-update-icon-cache /usr/share/icons/hicolor/ -t

