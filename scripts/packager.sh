#!/bin/bash

path="../build/usr/share/plank-adp"
mkdir -p $path
mkdir -v $path/ui
mkdir -v $path/bin
mkdir -p ../build/usr/bin/
mkdir -p ../build/usr/share/applications/
mkdir -p ../build/usr/share/icons/hicolor/128x128/apps
mkdir -p ../build/usr/share/plank/themes/Wallpaper
cp -v ../ui/form1.glade $path/ui
cp -v ../src/main.py $path/bin
cp -v ../src/utils.py $path/bin
cp -v ../base.theme $path
cp -v plank-adp ../build/usr/bin/
cp -v ../src/plank-adp.desktop ../build/usr/share/applications/
cp -v ../ui/plank-adp.svg ../build/usr/share/icons/hicolor/128x128/apps
chmod a=+rwx $path
chmod 0655 ../build/usr/share/icons/hicolor/128x128/apps/plank-adp.svg
chmod 0655 ../build/usr/share/plank/themes/Wallpaper
