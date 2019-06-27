#!/usr/bin/env python3
"""
Based on:
https://developer.gnome.org/gnome-devel-demos/stable/textview.py.html.en
"""
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gio
import sys


class MyTextView(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="TextView Example", application=app)
        self.set_border_width(10)
        self.set_default_size(450, 450)
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        buf = Gtk.TextBuffer()
        textview = Gtk.TextView(buffer=buf)
        textview.set_wrap_mode(Gtk.WrapMode.WORD)
        scrolled_window.add(textview)
        self.add(scrolled_window)


class TextViewExample(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self,
                                 application_id="io.Acry.TextViewExample",
                                 flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_activate(self):
        """shows the default first window of the application (like a new document).
           This corresponds to the application being launched by the desktop environment.
        """
        win = MyTextView(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)


if __name__ == '__main__':
    app = TextViewExample()
    exit_status = app.run(sys.argv)
    sys.exit(exit_status)
