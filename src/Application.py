from traits.api import *
from traitsui.api import *

from src.Converter import Converter
from src.Editor import Editor
from src.Animator import Animator


class Application(HasTraits):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    converter = Instance(Converter)
    animator = Instance(Animator)
    editor = Instance(Editor)

    def _converter_default(self):
        return Converter()

    def _animator_default(self):
        return Animator()

    def _editor_default(self):
        return Editor()

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
