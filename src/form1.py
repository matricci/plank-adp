#!/usr/bin/python3

from gi.repository import Gtk, Gio, Gdk
from PIL import Image
import urllib
import shutil
import gi
import os
gi.require_version("Gtk", "3.0")


class Handler():
    opacity = 255
    theme_color = []
    SCHEMA = 'org.gnome.desktop.background'
    KEY = 'picture-uri'

    def __init__(self, *args):
        button.set_sensitive(False)
        matchcheck.set_active(True)
        opacitydisplay.set_sensitive(False)

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
        if matchcheck.get_active() == True:
            self.set_wallpaper(filechooser.get_uri())
            self.get_theme_color(filechooser.get_uri()[7:])
            self.set_theme()
        else:
            self.get_theme_color("none")
            self.set_theme()

    def cancelbutton_clicked(self, button):
        Gtk.main_quit()

    def matchcheck_toggled(self, matchcheck):
        if matchcheck.get_active() == True:
            opacitydisplay.set_sensitive(False)
            filechooser.set_sensitive(True)
            if filechooser.get_uri() != None:
                button.set_sensitive(True)
            else:
                button.set_sensitive(False)

        else:
            opacitydisplay.set_sensitive(True)
            filechooser.set_sensitive(False)
            button.set_sensitive(True)


    # This function gives the user an exemple of what the opacity will look like
    def opacityadj_value_changed(self, adjustment='opacityadj'):
        if self.theme_color != []:
            if self.theme_color[0] == "rgb":
                color = Gdk.RGBA()
                color.parse("rgba({},{})".format(
                    self.theme_color[1], opacityadj.get_value() / 255).replace(',', ', '))
            else:
                (r, g, b) = self.theme_color
                # looks like shit, I know :)
                color = Gdk.RGBA(r / 255, g/255, b/255,
                                 (opacityadj.get_value() / 255.0))
        else:
            color = Gdk.RGBA(0, 0, 0, opacityadj.get_value() / 255.0)

        opacitydisplay.set_rgba(color)
        self.opacity = opacityadj.get_value()

    def opacitydisplay_color_set(self, opacitydisplay):
        displaycolor = opacitydisplay.get_rgba()
        self.theme_color = ["rgb", displaycolor.to_string()[4:-1]]
    ##

    def get_theme_color(self, filename):
        border_radius = int(borderadj.get_value())
        ## Check if user has selected match wallpaper or not
        if matchcheck.get_active() == True:
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
            color = ('{};;{};;{};;{}'.format(
                *img.getpixel((0, 0)), float(self.opacity)))
        else:
            displaycolor = opacitydisplay.get_rgba().to_color()
            no_alpha = Gdk.RGBA()
            no_alpha.parse(displaycolor.to_string())
            color = "{};;{}".format(no_alpha.to_string()[
                4:-1].replace(",", ";;"), float(self.opacity))
        # Here starts the replacement part of the code ;)
        with open('../base.theme', 'r') as f:
            filedata = f.read()
            # first replace on the base the color that will be applied
            newcolor = filedata.replace("color", color)
            # then replace with the choosen border radius
            newbdrd = newcolor.replace("border_radius", str(border_radius))
        with open('../dock.theme', 'w') as f:
            f.write(newbdrd)

    def set_wallpaper(self, file):
        gsettings = Gio.Settings.new(self.SCHEMA)
        gsettings.set_string(self.KEY, file)

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
borderadj = builder.get_object("borderadj")
matchcheck = builder.get_object("matchcheck")
#
builder.connect_signals(Handler())
window.show_all()
Gtk.main()
