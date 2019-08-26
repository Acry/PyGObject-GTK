#!/usr/bin/env python3

"""
Use of GTK-SourceView 4
-- StyleSchemeChooserButton
"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gio
gi.require_version('GtkSource', '4')
from gi.repository import GtkSource
import sys

python_file = __file__


class MySourceView(Gtk.ApplicationWindow):

    def __init__(self, app):
        Gtk.Window.__init__(self, title="Source.View Example", application=app)
        self.set_border_width(10)
        self.set_default_size(450, 450)

        bb = Gtk.ButtonBox()
        bb.set_orientation(Gtk.Orientation.HORIZONTAL)
        bb.set_spacing(2)

        swb = GtkSource.StyleSchemeChooserButton.new()

        bb.add(swb)
        bb.set_child_secondary(swb, True)
        box = Gtk.Box()
        box.set_orientation(Gtk.Orientation.VERTICAL)
        box.set_spacing(5)
        box.pack_start(bb, False, False, 0)

        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        box.pack_start(scrolled_window, True, True, 0)

        sourceview = GtkSource.View.new()
        buf = sourceview.get_buffer()
        lm = GtkSource.LanguageManager()
        buf.set_language(lm.get_language("python3"))
        scrolled_window.add(sourceview)
        sourcefile = GtkSource.File()
        sourcefile.set_location(Gio.File.new_for_path(python_file))
        loader = GtkSource.FileLoader.new(buf, sourcefile)
        loader.load_async(0, None, None, None, None, None)
        wrap_mode = Gtk.WrapMode(2)
        sourceview.set_wrap_mode(wrap_mode)
        self.add(box)


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
