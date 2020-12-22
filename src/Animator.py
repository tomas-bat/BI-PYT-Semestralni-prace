import os

from pyface.constant import OK
from pyface.directory_dialog import DirectoryDialog
from traits.api import *
from traitsui.api import *


class Animator(HasTraits):
    def __init__(self, application, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.application = application


    dialog = DirectoryDialog()

    test = Button('Test')

    select_converted_folder = Button('Select folder with converted pictures')

    display_converted_folder_path = Str('<folder not selected>')

    font_size = Range(1, 10)

    show_animation = Button('Show animation')

    fps = Range(1, 100, value=30)

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
                            Item('fps', label='FPS:')
                        )
                    ),
                    Item('show_animation', show_label=False)
                )
            ),
            Item('shower_info_label', show_label=False, style='readonly')
        )
    )
