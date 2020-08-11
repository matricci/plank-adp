#!/bin/bash


## Prepare the fakeroot tree ##
rm -rf ../build/usr
path="../build/usr/share/plank-adp"
mkdir -p $path
mkdir -v $path/ui
mkdir -v $path/bin
mkdir -p ../build/usr/bin/
mkdir -p ../build/usr/share/applications/
mkdir -p ../build/usr/share/icons/hicolor/128x128/apps
cp -v ../ui/form1.glade $path/ui
cp -v ../src/main.py $path/bin
cp -v ../src/utils.py $path/bin
cp -v ../base.theme $path
cp -v plank-adp ../build/usr/bin/
cp -v ../src/plank-adp.desktop ../build/usr/share/applications/
cp -v ../ui/plank-adp.svg ../build/usr/share/icons/hicolor/128x128/apps
chmod a=+rwx $path
chmod 0655 ../build/usr/share/icons/hicolor/128x128/apps/plank-adp.svg
## ====================  ##

## Build the packages ##
cd ..
rm plank-adp*
/usr/bin/dpkg-deb --build build
mv build.deb plank-adp_1.0.1.deb
fpm  -s deb -t rpm --no-auto-depends -d 'plank' -d 'python3-gobject' -d 'python3-pillow' -d 'python3-cairo' plank-adp_1.0.1.deb
## ====================  ##
