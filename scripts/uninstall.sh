#!/bin/bash 

path="/usr/share/plank-adp"
sudo rm -rfv $path
sudo rm -v /usr/share/applications/plank-adp.desktop
sudo rm -v /usr/share/icons/hicolor/128x128/plank-adp.svg

sudo update-desktop-database /usr/share/applications/
sudo gtk-update-icon-cache /usr/share/icons/hicolor/ -t
