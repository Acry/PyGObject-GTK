#!/usr/bin/env python3

"""
Use of GTK-SourceView 4
-- StyleSchemeChooser
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

    def style_cb(self, ssw, ev, buf, cb):
        self.cur_style = ssw.get_style_scheme()
        buf.set_style_scheme(self.cur_style)
        cb.set_label(self.cur_style.get_id())

    def cb_active(self, button, dialog, ssw):
        ssw.show()
        dialog.show()

    def dia_resp(self, a, b, buf, cb):
        """
        https://lazka.github.io/pgi-docs/#Gtk-3.0/enums.html#Gtk.ResponseType
        OK= -5
        Returned by OK buttons in GTK+ dialogs
        CANCEL= -6
        Returned by Cancel buttons in GTK+ dialogs
        """
        if b == -5:
            a.hide
            self.old_style = self.cur_style
        if b == -6:
            buf.set_style_scheme(self.old_style)
        cb.set_label(self.old_style.get_id())
        a.hide()

    def dia_close(self, dia, ev):
        return True

    def __init__(self, app):
        Gtk.Window.__init__(self, title="Source.View Example", application=app)
        self.set_border_width(10)
        self.set_default_size(450, 450)
        self.old_style = None
        self.cur_style = None

        bb = Gtk.ButtonBox()
        bb.set_orientation(Gtk.Orientation.HORIZONTAL)
        bb.set_spacing(2)

        cb = Gtk.Button.new()
        ssw = GtkSource.StyleSchemeChooserWidget.new()
        dw = Gtk.Dialog.new()
        dw.add_button("_Set", Gtk.ResponseType.OK)
        dw.add_button("_Leave", Gtk.ResponseType.CANCEL)
        dw.set_transient_for(self)
        dw.set_title("Style Chooser")
        ca = dw.get_content_area()
        ca.pack_start(ssw, True, True, 0)
        cb.connect("clicked", self.cb_active, dw, ssw)

        bb.add(cb)
        bb.set_child_secondary(cb, True)
        box = Gtk.Box()
        box.set_orientation(Gtk.Orientation.VERTICAL)
        box.set_spacing(5)
        box.pack_start(bb, False, False, 0)

        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        box.pack_start(scrolled_window, True, True, 0)

        sourceview = GtkSource.View.new()
        buf = sourceview.get_buffer()
        ssw.connect("button-release-event", self.style_cb, buf, cb)
        dw.connect("response", self.dia_resp, buf, cb)
        dw.connect("delete-event", self.dia_close)
        self.old_style = buf.get_style_scheme()
        cb.set_label(self.old_style.get_id())
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
