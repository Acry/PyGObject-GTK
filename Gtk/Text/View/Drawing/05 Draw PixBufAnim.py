#!/usr/bin/env python3

u"""05 Draw PixBufAnim.py
"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gio
from gi.repository.GdkPixbuf import PixbufAnimation
from gi.repository import Gdk
from gi.repository import GLib
import sys
import os

ICON_IMAGE = os.path.join('gtk-logo.svg')
FOURIER_IMAGE = os.path.join("Fourier_series_square_wave_circles_animation.gif")
CSS_FILE = os.path.join('view.css')


class MyTextView(Gtk.ApplicationWindow):
    pb = None

    def __init__(self, app):
        Gtk.Window.__init__(self, title="TextView Example", application=app)
        self.set_border_width(10)
        self.set_default_size(450, 450)
        self.set_icon_from_file(ICON_IMAGE)
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        buf = Gtk.TextBuffer()
        textview = Gtk.TextView(buffer=buf)
        textview.set_wrap_mode(Gtk.WrapMode.WORD)
        scrolled_window.add(textview)
        textview.connect('draw', self.draw_cb)
        # region CSS
        style_provider = Gtk.CssProvider()
        style_provider.load_from_path(CSS_FILE)
        context = textview.get_style_context()
        context.add_provider(
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
        # endregion
        anim = PixbufAnimation.new_from_file(FOURIER_IMAGE)
        _iter = anim.get_iter()
        pb = _iter.get_pixbuf()
        self.pb = pb
        del pb
        delay = _iter.get_delay_time()
        GLib.timeout_add(delay, self.frame_update, _iter, textview)
        self.add(scrolled_window)

    def frame_update(self, _iter, textview):
        if _iter.advance():
            print("Advance")
            pb = _iter.get_pixbuf()
            self.pb = _iter.get_pixbuf()
            del pb
            textview.queue_draw()
        delay = _iter.get_delay_time()
        GLib.timeout_add(delay, self.frame_update, _iter, textview)

    def draw_cb(self, widget, cr):
        gdk_window = widget.get_window(1)
        surf = Gdk.cairo_surface_create_from_pixbuf(self.pb, 1, gdk_window)
        if surf:
            cr.set_source_surface(surf, 50, 50)
            cr.paint()
            del surf
        return False


class TextViewExample(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self,
                                 application_id="io.Acry.TextViewExample",
                                 flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_activate(self):
        win = MyTextView(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)


if __name__ == '__main__':
    app = TextViewExample()
    exit_status = app.run(sys.argv)
    sys.exit(exit_status)


