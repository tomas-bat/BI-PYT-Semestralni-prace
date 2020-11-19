from traits.api import *
from traitsui.api import *

from src.Converter import Converter
from src.Editor import Editor
from src.Animator import Animator


class Application(HasTraits):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    converter = Instance(Converter)
    animator = Animator()
    editor = Editor()

    view = View(
        Group(
            Item("converter", show_label=False, style='custom', dock="tab"),
            Item("animator", style='custom', show_label=False, dock="tab"),
            Item("editor", style='custom', show_label=False, dock="tab"),
            layout='tabbed'
        ),
        resizable=True,
        title='ASCII-art generator'
    )


