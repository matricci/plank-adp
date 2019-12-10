#!/usr/bin/python3

from PIL import Image
import urllib
import shutil
import os
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Handler():
    def onDestroy(self, *args):
        Gtk.main_quit()
        quit()

    def on_Window_destroy(self, *args):
        Gtk.main_quit()

    def filechooser_file_activated(self, widget):
        pass

    def aboutbutton_clicked(self, widget):
        aboutwin.show()

    def closebutton_clicked(self, button):
        aboutwin.hide()

    def button_clicked(self, button):
        self.set_wallpaper()
        self.get_theme_color()
        self.set_theme()

    def cancelbutton_clicked(self, button):
        Gtk.main_quit()

    def get_theme_color(self):
        filename = filechooser.get_uri()[7:]
        if(filename == "None"):
            print("Select an image")
        print(filename)
        image = Image.open(filename.replace("%20", " "))
        width, height = image.size  # Get image size
        # Get 10% of bottom image
        dock = int(height - round(height * 0.10))
        #
        cropped_image = image.crop((0, dock, width, height))  # Cut the image
        img2 = cropped_image.resize((1, 1), Image.ANTIALIAS)  # Resize to 1x1, same as average
        color = img2.getpixel((0, 0))  # Get the color
        color2 = ('{};;{};;{};;255'.format(*color))  # Format the color to replace inside 'dock.theme'
        # Here starts the replacement part of the code ;)
        with open('../base.theme', 'r') as f:
            filedata = f.read()
            newdata = filedata.replace("color", color2)
        with open('../dock.theme', 'w') as f:
            f.write(newdata)

    def set_wallpaper(self):
        if (os.environ.get("XDG_CURRENT_DESKTOP") == "MATE"):
            file = filechooser.get_uri()[7:]
            os.system("dconf write /org/mate/desktop/background/picture-filename \"'{}'\" " .format(file))

        if(os.environ.get("XDG_CURRENT_DESKTOP") == "GNOME"):
            file = filechooser.get_uri()
            os.system("dconf write /org/gnome/desktop/background/picture-uri \"'{}'\" ".format(file))

        if(os.environ.get("XDG_CURRENT_DESKTOP") == "Pantheon"):
            file = filechooser.get_uri()
            os.system("dconf write /org/gnome/desktop/background/picture-uri \"'{}'\" ".format(file))

    def set_theme(self):
        home = os.environ.get("HOME")
        shutil.copy("../dock.theme", "{}/.local/share/plank/themes/Wallpaper".format(home))


builder = Gtk.Builder()
builder.add_from_file("../ui/form1.glade")
builder.connect_signals(Handler())
window = builder.get_object("Window")
filechooser = builder.get_object("filechooser")
aboutwin = builder.get_object("about_window")
window.show_all()
Gtk.main()
