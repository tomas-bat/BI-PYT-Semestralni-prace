from traits.api import *
from traitsui.api import *

from src.FileDialog import FileDialog


class Converter(HasTraits):
    width = Int()
    convert = Button()
    load = Button()
    load_custom_chars = Button("Load custom character set")
    chars_dialog = Instance(Handler)

    def _load_custom_chars_fired(self):
        self.chars_dialog.edit_traits()

    def _chars_dialog_default(self):
        return FileDialog()

    view = View(
        VGroup(
            HGroup(
                Item("load_custom_chars", show_label=False)
            ),
            HGroup(
                Item("load", show_label=False),
                Item("width"),
                Item("convert", show_label=False)
            )
        )
    )
