
# Highlight Styles



## Set and get Style Schemes

Get and set Scheme to buffer:<br>
`buffer.get_style_scheme()`<br>
`buffer.set_style_scheme()`<br>

The name as string is provided by `get_id()`


## StyleSchemeManager

A Highlight-Style loader.

Construct a manager:<br>
`ssm = GtkSource.StyleSchemeManager.new()`

Print search pathes:
```python
for path in ssm.get_search_path():
    print(path)
```

Available Schemes are printed with:<br>
`print(ssm.get_scheme_ids())`

## Links

<https://developer.gnome.org/gtksourceview/stable/style-reference.html>
<https://wiki.gnome.org/Projects/GtkSourceView/StyleSchemes>
<https://github.com/jonocodes/GtkSourceSchemer>
<https://www.gnome-look.org/browse/cat/279/>
<https://delightlylinux.wordpress.com/2015/03/25/gedit-themes/>