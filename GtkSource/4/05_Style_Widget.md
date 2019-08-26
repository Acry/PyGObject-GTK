# StyleSchemeChooser

I tried to get the GtkSource.StyleSchemeChooserButton to work.
I have no clue how work with it programmatically.

The Documentation is missing, everything is just inserted automatically.
https://lazka.github.io/pgi-docs/#GtkSource-4/classes/StyleSchemeChooserButton.html#GtkSource.StyleSchemeChooserButton

I think the button should take a widget as argument.

ssw = GtkSource.StyleSchemeChooserWidget.new()
swb = GtkSource.StyleSchemeChooserButton.new(ssw)

However, you can watch the Button in `05_Style_Widget_Button.py`.
If you know how it works, let me know. `05_Style_Widget.py` is a workaround to deal with the widget and create a similar dialog/behaviour.

You can ignore the Button Box here, it is not relevant.

I created a button and the label is the active style.
The Style-Widget is embedded in the content area of a dialog.

The button-callback shows the dialog and style-widget.
The dialog callback applies or cancels the style-choice, sets the label of the button and hides the dialog.

The `dia_close`-CB prevents that the dialog is destroyed.

The `style_cb` reacts on a style click and sets the label of the button, too.

