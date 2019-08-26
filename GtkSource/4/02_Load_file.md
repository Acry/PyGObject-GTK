# Source View File Loading

To load a file into the buffer one needs the buffer object and a GtkSource.File.

`buf = sourceview.get_buffer()  # get buffer `

`sourcefile = GtkSource.File.new()  # construct GtkSource.File`

Now the GtkSource.File's location need to be set

`set_location(location)`

Parameters:
location (Gio.File or None) – the new Gio.File, or None.

As GtkSource.File expects a Gio.File one have to deal with that concept, too.

sourcefile.set_location(Gio.File.new_for_path(python_file))

I used the __file__ attribute as path.

I am not diving into the loader class here, it loads the file and sets the buffer.

```python
loader = GtkSource.FileLoader.new(buf, sourcefile)
loader.load_async(0, None, None, None, None, None)
```

After that the source-code is available in the buffer.

No need to call `buffer.set_text()`

As one can see in `02_load_file.py` a simple file read does the same job, for now.
