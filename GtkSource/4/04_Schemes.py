#!/usr/bin/env python3

"""
Use of GTK-SourceView 4
-- Style / StyleSchemeManager
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
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        sourceview = GtkSource.View.new()
        buf = sourceview.get_buffer()
        scrolled_window.add(sourceview)
        sourcefile = GtkSource.File()
        sourcefile.set_location(Gio.File.new_for_path(python_file))
        lang_manager = GtkSource.LanguageManager()
        buf.set_language(lang_manager.get_language("python3"))

        print("Using Scheme:", buf.get_style_scheme().get_id())
        prev_scheme = buf.get_style_scheme().get_id()

        ssm = GtkSource.StyleSchemeManager.new()
        # print(ssm.get_search_path())
        for path in ssm.get_search_path():
            print(path)
        print(ssm.get_scheme_ids())
        scheme = ssm.get_scheme(ssm.get_scheme_ids()[5])
        if not scheme:
            scheme = ssm.get_scheme(prev_scheme)
        buf.set_style_scheme(scheme)
        print("Now using Scheme:", buf.get_style_scheme().get_id())

        loader = GtkSource.FileLoader.new(buf, sourcefile)
        loader.load_async(0, None, None, None, None, None)
        wrap_mode = Gtk.WrapMode(2)
        # https://lazka.github.io/pgi-docs/#Gtk-3.0/enums.html#Gtk.WrapMode
        sourceview.set_wrap_mode(wrap_mode)
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
