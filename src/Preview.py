import os
from time import time

from pyface.constant import OK
from pyface.directory_dialog import DirectoryDialog
from traits.api import *
from traitsui.api import *

from src.AsciiShower import AsciiShower


class Preview(HasTraits):
    def __init__(self, application, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.application = application
        self.images.append('<none>')

    # A platform-independent dialog to select a directory with images:
    dialog = DirectoryDialog()

    previous_image = Button('<')

    current_image = Str()

    images = List(Str())

    next_image = Button('>')

    show_image = Button('Show Image')

    font_size = Range(1, 10)

    select_converted_folder = Button('Select folder with converted pictures')

    selected_converted_folder = '__none__'

    display_converted_folder_path = Str('<folder not selected>')

    shower_info_label = Str('No ascii pictures to show.')

    def _select_converted_folder_fired(self):
        result = self.dialog.open()
        if result == OK:
            self.selected_converted_folder = self.dialog.path
            if len(self.dialog.path) > 40:
                self.display_converted_folder_path = '...' + self.dialog.path[-40:]
            else:
                self.display_converted_folder_path = self.dialog.path
            pathdir = os.listdir(self.dialog.path)
            self.images.clear()
            at_least_one = False
            for item in pathdir:
                # Only append non-directories and files ending with '.ascii'
                if not os.path.isdir(os.path.join(self.dialog.path, item)) and item[-6:] == '.ascii':
                    self.images.append(item)
                    at_least_one = True
            if not at_least_one:
                self.images.append('<none>')
            else:
                self.current_image = self.images[0]

    def _show_image_fired(self):
        ascii = ''
        path = self.selected_converted_folder + '/' + self.current_image
        with open(str(path), mode='r+', encoding='utf-8') as f:
            ascii = f.read()
        shower = AsciiShower(ascii)
        style_sheet = '*{font-size:' + str(self.font_size) + 'px; font-family:"Menlo"}'
        view = View(
            Item('ascii', style='readonly', show_label=False, style_sheet=style_sheet)
        )
        shower.configure_traits(view=view)

    view = View(
        VGroup(
            VGroup(
                HGroup(
                    Item('select_converted_folder', show_label=False),
                    Item('display_converted_folder_path', show_label=False, style='readonly')
                ),
                HGroup(
                    VGroup(
                        HGroup(
                            Item('font_size', label='Font size:'),
                        ),
                        HGroup(
                            Item('current_image', editor=CheckListEditor(name='images')),
                        )
                    ),
                    Item('show_image', show_label=False)
                )
            ),
            Item('shower_info_label', show_label=False, style='readonly')
        )
    )