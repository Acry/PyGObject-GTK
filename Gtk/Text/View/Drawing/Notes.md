

# Drawing on a GTK Textview in Python

This series is about Drawing with Cairo on GTK Textview, regarding CSS.

Usually the Textview is a child of a Scrolled Window.

```mono
Gtk.ScrolledWindow
  ╰──Gtk.TextView
```


The Textview itself is complex as one can see in the CSS Nodes.

##### Textview CSS nodes

```mono
textview.view
├── border.top
├── border.left
├── text
│   ╰── [selection]
├── border.right
├── border.bottom
╰── [window.popup]
```

The CSS-File is crucial to see our drawings

```css
textview.view
, text {
background-color: transparent;
}
```

Drawing happens on the draw signal of the widget.

Hook up to that event: `widget.connect("draw", cb-name)`

In the CB I 'return False', because I do not want to prevent further handling of the `draw signal`.

Check out what happens if one return `True`*[]: 

## Examples
[Draw a Line](./"01 Draw Line.md")

[Draw a PixBuf](./"02 Draw Pixbuf.md")

[Translate Cooordinates](./"03 Coordinates.md")

[Move PixBuf](./"04 Move Pixbuf.md")

[Draw a PixBufAnim](./"05 Draw PixbufAnim.md")


##Links

Drawing in GTK<br>
https://blog.gtk.org/2016/06/15/drawing-in-gtk/

The GTK Drawing Model<br>
https://developer.gnome.org/gtk3/stable/chap-drawing-model.html