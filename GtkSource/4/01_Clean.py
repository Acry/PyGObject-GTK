#!/usr/bin/env python3

"""
Use of GTK-SourceView 4
-- A Clean View
"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gio
gi.require_version('GtkSource', '4')
from gi.repository import GtkSource
import sys


class MySourceView(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="Source.View Example", application=app)
        self.set_border_width(10)
        self.set_default_size(450, 450)
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        sourceview = GtkSource.View.new()
        sourceview.set_wrap_mode(Gtk.WrapMode.WORD)
        scrolled_window.add(sourceview)
        self.add(scrolled_window)


class SourceViewExample(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self,
                                 application_id="io.Acry.SourceViewExample",
                                 flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_activate(self):
        """shows the default first window of the application (like a new document).
           This corresponds to the application being launched by the desktop environment.
        """
        win = MySourceView(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)


if __name__ == '__main__':
    app = SourceViewExample()
    exit_status = app.run(sys.argv)
    sys.exit(exit_status)
