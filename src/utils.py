import os
import shutil
from gi.repository import Gio

GNOME_SCHEMA = 'org.gnome.desktop.background'
GNOME_KEY = 'picture-uri'


def get_desktop_environment():
    env = os.environ.get("XDG_CURRENT_DESKTOP")
    return env


def check_theme_folder():
    if(os.path.exists('/{}/.local/share/plank/themes/Wallpaper/'.format(os.environ.get('HOME'))) == False):
        os.system("mkdir -p ~/.local/share/plank/themes/Wallpaper")


def set_wallpaper(file):
    env = get_desktop_environment()
    if env == "GNOME" or env == "Pantheon":
        gsettings = Gio.Settings.new(GNOME_SCHEMA)
        gsettings.set_string(GNOME_KEY, file)
    elif env == "MATE":
        gsettings = Gio.Settings.new("org.mate.background")
        gsettings.set_string("picture-filename", file[7:])
