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

if [ $LANG == "pt_BR.UTF-8" ];then 
	cp -v form1.glade.pt_BR form1.glade

else 
	cp -v form1.glade.en form1.glade
fi
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
sudo cp -v ../ui/plank-adp.png /usr/share/icons/hicolor/128x128/
sudo chmod a=+rwx $path

# Change the theme to "Wallpaper"
dconf write /net/launchpad/plank/docks/dock1/theme "'Wallpaper'"


