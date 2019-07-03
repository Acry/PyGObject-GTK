#!/usr/bin/env python3
"""
Draw Line.py

Drawing on a Textview Window.

Draw a static red horizontal line.
"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gio
import sys
import os

ICON_IMAGE = os.path.join('gtk-logo.svg')
CSS_FILE = os.path.join('view.css')
TEXT = __doc__


class MyTextView(Gtk.ApplicationWindow):

    def __init__(self, app):
        Gtk.Window.__init__(self, title="DrawLine", application=app)
        self.set_border_width(10)
        self.set_default_size(450, 450)
        self.set_icon_from_file(ICON_IMAGE)
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        buf = Gtk.TextBuffer()
        buf.set_text(TEXT)
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
        self.add(scrolled_window)

    def draw_cb(self, widget, cr):
        alloc = widget.get_allocation()
        buf = widget.get_buffer()
        text_iter = buf.get_iter_at_line(4)
        iter_rect = widget.get_iter_location(text_iter)
        y = iter_rect.y
        x = alloc.width
        cr.set_line_width(1)
        cr.set_source_rgba(1, 0, 0)
        cr.move_to(0, y + 0.5)
        cr.line_to(x, y + 0.5)
        cr.stroke()
        return False


class TextViewExample(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self,
                                 application_id="io.Acry.DrawLine",
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
