import os

from pyface.constant import OK
from pyface.directory_dialog import DirectoryDialog
from traits.api import *
from traitsui.api import *

from src.AnimationShower import AnimationShower


class Animator(HasTraits):
    def __init__(self, application, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.application = application

    dialog = DirectoryDialog()

    test = Button('Test')

    select_converted_folder = Button('Select folder with converted pictures')

    display_converted_folder_path = Str('<folder not selected>')

    font_size = Range(1, 10, value=3)

    show_animation = Button('Show animation')

    fps = Range(1, 100, value=30)

    shower_info_label = Str('No ascii pictures to show.')

    selected_converted_folder = '__none__'

    no_images = True

    def _select_converted_folder_fired(self):
        result = self.dialog.open()
        if result == OK:
            self.selected_converted_folder = self.dialog.path
            if len(self.dialog.path) > 40:
                self.display_converted_folder_path = '...' + self.dialog.path[-40:]
            else:
                self.display_converted_folder_path = self.dialog.path
            pathdir = os.listdir(self.dialog.path)

            self.ascii_list = list()
            for filename in sorted(os.listdir(self.selected_converted_folder)):
                if filename[-6:] == '.ascii':
                    with open(os.path.join(self.selected_converted_folder, filename), mode='r+', encoding='utf-8') as f:
                        self.ascii_list.append(f.read())

            if len(self.ascii_list) > 0:
                self.no_images = False
                self.shower_info_label = 'Images loaded.'
            else:
                self.no_images = True
                self.shower_info_label = 'No ascii images found.'

    def _show_animation_fired(self):
        if self.selected_converted_folder == '__none__':
            self.shower_info_label = 'No folder has been selected.'
            return

        if self.no_images:
            self.shower_info_label = 'No ascii images found.'
            return

        shower = AnimationShower(self.ascii_list, self.fps)
        style_sheet = '*{font-size:' + str(self.font_size) + 'px; font-family:"Menlo"}'
        view = View(
            Item('play', show_label=False),
            Item('ascii_label', style='readonly', springy=True, show_label=False, style_sheet=style_sheet),
            title='Animation'
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
                            Item('fps', label='FPS:')
                        )
                    ),
                    Item('show_animation', show_label=False)
                )
            ),
            Item('shower_info_label', show_label=False, style='readonly')
        )
    )
