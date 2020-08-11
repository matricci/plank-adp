import os
import shutil
from gi.repository import Gio

GNOME_SCHEMA = 'org.gnome.desktop.background'
GNOME_KEY = 'picture-uri'


def get_desktop_environment():
    env = os.environ.get("XDG_CURRENT_DESKTOP")
    return env


def set_theme():
    try:
        shutil.copy("../dock.theme",
                    "{}/.local/share/plank/themes/Wallpaper/dock.theme".format(os.environ.get("HOME")))
    except FileNotFoundError:
        os.system("mkdir -p ~/.local/share/plank/themes/Wallpaper")
        print("The theme folderhas been created, try again")


def set_wallpaper(file):
    env = get_desktop_environment()
    if env == "GNOME" or env == "Pantheon":
        gsettings = Gio.Settings.new(GNOME_SCHEMA)
        gsettings.set_string(GNOME_KEY, file)
    elif env == "MATE":
        gsettings = Gio.Settings.new("org.mate.background")
        gsettings.set_string("picture-filename", file[7:])
