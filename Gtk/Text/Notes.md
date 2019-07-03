# GTK Text Concept - Intro

The Text Widget is part of the GTK's text editing system.

One can either use a Gtk.TextView or GtkSource.View to display Text.

TextView widgets and their associated objects: TextBuffers, TextMarks, TextIters, TextTags and the TextTagTables - provide a framework for multiline text editing.

A TextBuffer contains the text which is displayed by one or more TextView widgets.
Marks and Iters help to navigate and mark regions in a TextBuffer.
Marks are persistent over buffer changes while Iters are temporary.
A tag can do actions on Iters and marks.

Within GTK text is encoded in UTF-8 which means that one character may be encoded as multiple bytes.
Within a TextBuffer it is necessary to differentiate between the character counts (called offsets) and the byte counts (called indexes).

Usually the view is shown in a Scrolled window.

## Drawing on a Textview

[Notes](./View/Drawing/Notes.md)

## Links

A Demo on the GNOME's Developer Site:
https://developer.gnome.org/gnome-devel-demos/stable/textview.py.html.en

Additional Informations:
https://gitlab.gnome.org/GNOME/gtk/blob/master/docs/text_widget_internals.txt
