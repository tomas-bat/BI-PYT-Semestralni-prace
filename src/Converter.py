from pyface.constant import OK
from pyface.directory_dialog import DirectoryDialog
from traits.api import *
from traitsui.api import *


class Converter(HasTraits):
    # Max width for the conversion:
    width = Int()

    convert = Button()

    load = Button()

    select_folder = Button('Select folder with pictures')

    display_folder_path = Str('<folder not selected>')

    # A platform-independent dialog to select a directory with images:
    dialog = DirectoryDialog()

    # If user clicks on 'Select folder with pictures':
    def _select_folder_fired(self):
        result = self.dialog.open()
        if result == OK:
            if len(self.dialog.path) > 40:
                self.display_folder_path = '...' + self.dialog.path[-40:]
            else:
                self.display_folder_path = self.dialog.path

    view = View(
        VGroup(
            HGroup(
                Item('select_folder', show_label=False),
                Item('display_folder_path', style='readonly', show_label=False)
            ),
            HGroup(
                Item('load', show_label=False),
                Item('width'),
                Item('convert', show_label=False)
            )
        )
    )
