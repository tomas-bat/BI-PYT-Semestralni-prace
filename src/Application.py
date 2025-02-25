from pyface.constant import OK
from pyface.file_dialog import FileDialog
from traits.api import *
from traitsui.api import *

from src.Preview import Preview
from src.Converter import Converter
from src.Animator import Animator


class Application(HasTraits):
    converter = Instance(Converter)
    animator = Instance(Animator)
    preview = Instance(Preview)

    select_file = Button('Select file with custom character set')

    display_char_set = Str('<default character set>')

    invert = Bool()

    dialog = FileDialog()

    def _select_file_fired(self):
        result = self.dialog.open()
        if result == OK:
            if len(self.dialog.path) > 40:
                self.display_char_set = '...' + self.dialog.path[-40:]
            else:
                self.display_char_set = self.dialog.path

    def _converter_default(self):
        return Converter(self)

    def _animator_default(self):
        return Animator(self)

    def _preview_default(self):
        return Preview(self)

    view = View(
        VGroup(
            VGroup(
                HGroup(
                    Item('select_file', show_label=False),
                    Item('display_char_set', show_label=False, style='readonly')
                ),
                Item('invert', label='Invert characters (suitable for dark background)')
            ),
            Group(
                Item('converter', show_label=False, style='custom', dock='tab'),
                Item('preview', show_label=False, style='custom', dock='tab'),
                Item('animator', style='custom', show_label=False, dock='tab'),
                layout='tabbed'
            )
        ),
        resizable=True,
        title='ASCII-art generator'
    )
