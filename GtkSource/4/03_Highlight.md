# Syntax Highlighting

To actually make Syntax Highlighting work, one needs the LanguageManager.

Not going in detail here how to figure the programming language to show.

Contruct LM
lang_manager = GtkSource.LanguageManager()

Get Language-Object:
lang = lang_manager.get_language("python")

Set buffer language
buf.set_language(lang)

`print(lang.get_id())` return python as string, but one can't just use a sting as argument to set_language.

I think a good API would accept a string and create an object (if needed) itself.

As one can see in `03_sourceview_highlight_b.py`, Syntax Highlighting works with a plain loader, too.

## Links

If one needs a Language Definition, a tutorial is available:<br>
<https://developer.gnome.org/gtksourceview/stable/lang-tutorial.html>