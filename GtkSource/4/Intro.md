# Sourceview Widget

The Sourceview is an alternative Textview - it is specialised to view and edit source-code. One _really_ should have used [Gtk.Textview](../../Gtk/Text/Notes.md) before using GtkSource.View in code.


## Features

* Syntax highlighting with style schemes
* Line numbers
* Line marks
* Printing
* Highlight the current line
* Highlight the matching bracket
* Right margin
* Unlimited Undo/Redo
* Represent whitespace characters with symbols
* A minimap, which shows an overview of the text
* Auto completion
* Search and replace, with regex support
* Extended keyboard navigation (smart Home/End, smart backspace, auto indentation, line moving, etc.)


## Bindings

GObject Introspection, automatic bindings are available for JavaScript, Python, Vala, C++ and others.

Sourceview inherits from, and extends Gtk.TextView. It is not integral part of GTK, but in the GObject Introspection Framework.

Unfortunately, the automatic bindings are just rudimentary working.

```python
#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GObject

Button = Gtk.Button.new()
print(GObject.signal_list_names(Gtk.Button))
```

Lists the default signals one can use.
`('activate', 'pressed', 'released', 'clicked', 'enter', 'leave')`

```python
#!/usr/bin/env python3

import gi
from gi.repository import GObject
gi.require_version('GtkSource', '4')
from gi.repository import GtkSource

StyleWidget = GtkSource.StyleSchemeChooserWidget.new()
print(GObject.signal_list_names(GtkSource.StyleSchemeChooserWidget))
```
Prints nothing at all:
`()`

GtkSource doesn't conform fully to GObject yet.
Be aware that it can behave strange during dev-time.


## Usage

[Clean View](01_Clean.md)<br>
[Load File](02_Load_file.md)<br>
[Highlight Text/](03_Highlight.md)<br>
[Schemes](04_Schemes.md)<br>
[Style Widget](05_Style_Widget.md)<br>




## GtkSource Classes

GtkSource.Buffer<br>

GtkSource.Completion<br>
GtkSource.CompletionContext<br>
GtkSource.CompletionInfo<br>
GtkSource.CompletionItem<br>
GtkSource.CompletionWords<br>

GtkSource.File<br>
GtkSource.FileLoader<br>
GtkSource.FileSaver<br>

GtkSource.Gutter<br>
GtkSource.GutterRenderer<br>
GtkSource.GutterRendererPixbuf<br>
GtkSource.GutterRendererText<br>

GtkSource.Language<br>
GtkSource.LanguageManager<br>

GtkSource.Map<br>

GtkSource.Mark<br>
GtkSource.MarkAttributes<br>

GtkSource.PrintCompositor<br>

GtkSource.Region<br>
GtkSource.SearchContext<br>
GtkSource.SearchSettings<br>

GtkSource.SpaceDrawer<br>

GtkSource.Style<br>
GtkSource.StyleScheme<br>
GtkSource.StyleSchemeChooserButton<br>
GtkSource.StyleSchemeChooserWidget<br>
GtkSource.StyleSchemeManager<br>

GtkSource.Tag<br>
GtkSource.View<br>


## Links

Homepage        :	<https://wiki.gnome.org/Projects/GtkSourceView><br>
Bug Tracker     :	<https://gitlab.gnome.org/GNOME/gtksourceview/issues><br>
Mailing Lists   :	<https://mail.gnome.org/mailman/listinfo/gnome-devtools><br>

Python API-Ref:<br>
<https://lazka.github.io/pgi-docs/#GtkSource-4><br>

GNOME-Entries:<br>
<https://wiki.gnome.org/Projects/GtkSourceView><br>
<https://wiki.gnome.org/Projects/GtkSourceView/DevNotes><br>


C-Sources:<br>
<https://gitlab.gnome.org/GNOME/gtksourceview><br>

C-API:<br>
<https://developer.gnome.org/gtksourceview/><br>