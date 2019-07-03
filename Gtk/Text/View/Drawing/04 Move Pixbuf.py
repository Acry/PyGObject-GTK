#!/usr/bin/env python3

"""
04 Move Pixbuf.py

Hover the mouse over the pixbuf.
Press Control and move the pixbuf.

"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gio
from gi.repository.GdkPixbuf import Pixbuf
from gi.repository import Gdk
import sys
import os

ICON_IMAGE = os.path.join('gtk-logo.svg')
RED_APPLE = os.path.join('apple-red.png')
CSS_FILE = os.path.join('view.css')

TEXT = __doc__ + __doc__ + __doc__ + __doc__ + __doc__


def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) +
                x2 * (y3 - y1) +
                x3 * (y1 - y2)) / 2.0)


def check(x1, y1, x2, y2, x3,
          y3, x4, y4, x, y):
    # Calculate area of rectangle ABCD
    A = (area(x1, y1, x2, y2, x3, y3) +
         area(x1, y1, x4, y4, x3, y3))

    # Calculate area of triangle PAB
    A1 = area(x, y, x1, y1, x2, y2)

    # Calculate area of triangle PBC
    A2 = area(x, y, x2, y2, x3, y3)

    # Calculate area of triangle PCD
    A3 = area(x, y, x3, y3, x4, y4)

    # Calculate area of triangle PAD
    A4 = area(x, y, x1, y1, x4, y4);

    # Check if sum of A1, A2, A3
    # and A4 is same as A
    return A == A1 + A2 + A3 + A4


class Pix:
    pb = None
    x = None
    y = None

    def __init__(self, pb, x=0, y=0):
        self.pb = pb
        self.x = x
        self.y = y

    def add(self, pb, x=0, y=0):
        self.pb = pb
        self.x = x
        self.y = y


class MyTextView(Gtk.ApplicationWindow):
    pix_list = []
    moving_pic = False  # The moving pic
    pic_moving = None   # Is any pic moving?
    offset = 0

    def __init__(self, app):
        Gtk.Window.__init__(self, title="MovePixBuf", application=app)
        self.set_border_width(10)
        self.set_default_size(450, 450)
        self.set_icon_from_file(ICON_IMAGE)
        pb = Pixbuf.new_from_file(RED_APPLE)
        pix = Pix(pb, 50, 120)
        self.pix_list.append(pix)
        pix = Pix(pb, 150, 120)
        self.pix_list.append(pix)
        pix = Pix(pb, 250, 120)
        self.pix_list.append(pix)
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        buf = Gtk.TextBuffer()
        buf.set_text(TEXT)
        textview = Gtk.TextView(buffer=buf)
        textview.set_wrap_mode(Gtk.WrapMode.WORD)
        scrolled_window.add(textview)
        textview.connect('draw', self.draw_cb)
        textview.connect("button-press-event", self.button_press_callback)
        textview.connect("button-release-event", self.button_release_callback)
        textview.connect("motion-notify-event", self.on_motion)
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
        gdk_window = widget.get_window(1)
        for pix in self.pix_list:
            surf = Gdk.cairo_surface_create_from_pixbuf(pix.pb, 1, gdk_window)
            if surf:
                coords = widget.buffer_to_window_coords(1, pix.x, pix.y)
                cr.set_source_surface(surf, coords[0], coords[1])
                cr.paint()
                del surf
        return False

    def on_motion(self, widget, event):
        if self.moving_pic:
            b = self.get_border_width()
            b = int(b)
            # New Code instead of widget.get_pointer() - Wow!
            # I guess it is stupid to this in a CB.
            gdk_window = widget.get_window(1)
            display = Gdk.Display.get_default()
            seat = display.get_default_seat()
            pointer = seat.get_pointer()
            dev_pos = gdk_window.get_device_position(pointer)
            coords = dev_pos.x, dev_pos.y

            # coords = widget.get_pointer()
            # DeprecationWarning
            self.pic_moving.x = coords[0] - self.offset[0]
            self.pic_moving.y = coords[1] - b - self.offset[1]
            widget.queue_draw()

    def button_release_callback(self, widget, event, data=None):
        if self.moving_pic:
            self.moving_pic = False

    def button_press_callback(self, widget, event, data=None):
        accel_mask = Gtk.accelerator_get_default_mod_mask()
        if event.state & accel_mask == Gdk.ModifierType.CONTROL_MASK and event.button == 1:

            # New Code instead of widget.get_pointer() - Wow!
            # I guess it is stupid to this in a CB.
            gdk_window = widget.get_window(1)
            display = Gdk.Display.get_default()
            seat = display.get_default_seat()
            pointer = seat.get_pointer()
            dev_pos = gdk_window.get_device_position(pointer)
            coords = dev_pos.x, dev_pos.y

            # coords = widget.get_pointer()
            # DeprecationWarning
            for pix in self.pix_list:
                """
                D   A
                +---+
                |   |
                +---+
                C   B
                """
                w = pix.pb.get_width()
                h = pix.pb.get_height()
                ax = pix.x + w
                ay = pix.y
                bx = pix.x + w
                by = pix.y + h
                cx = pix.x
                cy = pix.y + h
                dx = pix.x
                dy = pix.y

                if check(ax, ay, bx, by, cx, cy, dx, dy, coords[0], coords[1]):
                    self.moving_pic = True
                    self.pic_moving = pix
                    b = self.get_border_width()
                    b = int(b)
                    self.offset = (coords[0]-self.pic_moving.x, (coords[1] - b) - self.pic_moving.y)
                    return True


class TextViewExample(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self,
                                 application_id="io.Acry.MovePixBuf",
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
