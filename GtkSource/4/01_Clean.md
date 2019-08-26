# A clean Source View

Setting up a clean Source View is very easy. Just take into account that it brings its own buffer-subclass, which is different from Gtk.TextBuffer.

The Source-Buffer's Inheritage:
GObject.Object
    Gtk.TextBuffer
        GtkSource.Buffer

To use Gtk.Source in an Gio.Application with Gtk you need following imports:

```python
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gio
gi.require_version('GtkSource', '4')
from gi.repository import GtkSource
```

The view itself is constructed with:
```python
view = GtkSource.View.new()
```

In the example I wrapped the view in a scrolled window, which is usual practice.

For now one won't note any difference in appearance.
