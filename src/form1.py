#!/usr/bin/python3

from gi.repository import Gdk
from gi.repository import Gtk
from PIL import Image
import urllib
import shutil
import os
import gi
gi.require_version("Gtk", "3.0")


class Handler():
    opacity = 255
    theme_color = []

    def __init__(self, *args):
        button.set_sensitive(False)

    # Bind signals
    def onDestroy(self, *args):
        Gtk.main_quit()
        quit()

    def on_Window_destroy(self, *args):
        Gtk.main_quit()

    def filechooser_file_set(self, widget):
        button.set_sensitive(True)
        self.get_theme_color(filechooser.get_uri()[7:])
        self.opacityadj_value_changed()

    def aboutbutton_clicked(self, widget):
        aboutwin.show()

    def closebutton_clicked(self, button):
        aboutwin.hide()

    def button_clicked(self, button):
        self.set_wallpaper(filechooser.get_uri())
        self.set_theme()

    def cancelbutton_clicked(self, button):
        Gtk.main_quit()

    # This function gives the user an exemple of what the opacity will look like
    def opacityadj_value_changed(self, adjustment='opacityadj'):
        if self.theme_color != []:
            (r, g, b) = self.theme_color
            # looks like shit, I know :)
            color = Gdk.RGBA(r / 255, g/255, b/255,
                             (opacityadj.get_value() / 255.0))
        else:
            color = Gdk.RGBA(0, 0, 0, opacityadj.get_value() / 255.0)

        opacitydisplay.set_rgba(color)
        self.opacity = opacityadj.get_value()
    ##

    def get_theme_color(self, filename):
        image = Image.open(filename.replace("%20", " "))
        # Get image size
        width, height = image.size
        # Get 10% of bottom image
        dock = int(height - round(height * 0.10))
        # Cut the image
        cropped_image = image.crop((0, dock, width, height))
        # Resize to 1x1, same as average
        img = cropped_image.resize((1, 1), Image.ANTIALIAS)
        # Format the color to replace inside 'dock.theme'
        self.theme_color = img.getpixel((0, 0))[:3]
        color = ('{};;{};;{};;{}'.format(*img.getpixel((0, 0)), self.opacity))
        # Here starts the replacement part of the code ;)
        with open('../base.theme', 'r') as f:
            filedata = f.read()
            newdata = filedata.replace("color", color)
        with open('../dock.theme', 'w') as f:
            f.write(newdata)

    def set_wallpaper(self, file):
        # Please redo this piece of crap using proper Gsettings
        if (os.environ.get("XDG_CURRENT_DESKTOP") == "MATE"):
            os.system(
                "dconf write /org/mate/desktop/background/picture-filename \"'{}'\" " .format(file[7:]))

        if(os.environ.get("XDG_CURRENT_DESKTOP") == "GNOME" or os.environ.get("XDG_CURRENT_DESKTOP") == "Pantheon"):
            os.system(
                "dconf write /org/gnome/desktop/background/picture-uri \"'{}'\" ".format(file))

    def set_theme(self):
        shutil.copy("../dock.theme",
                    "{}/.local/share/plank/themes/Wallpaper".format(os.environ.get("HOME")))


builder = Gtk.Builder()
builder.add_from_file("../ui/form1.glade")
# Import elements from the XML ui file
window = builder.get_object("Window")
filechooser = builder.get_object("filechooser")
aboutwin = builder.get_object("about_window")
button = builder.get_object("button")
opacityadj = builder.get_object("opacityadj")
opacitydisplay = builder.get_object("opacitydisplay")
#
builder.connect_signals(Handler())
window.show_all()
Gtk.main()
