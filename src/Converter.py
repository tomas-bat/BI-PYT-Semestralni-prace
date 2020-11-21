import os
from pprint import pprint
from threading import Thread
from time import sleep

from pyface.constant import OK
from pyface.directory_dialog import DirectoryDialog
from traits.api import *
from traitsui.api import *


class ConverterHandler(Thread):
    def run(self):
        pass


class Converter(HasTraits):
    def __init__(self, invert, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.invert = invert

    # Max width for the conversion:
    width = Int(0)

    convert = Button()

    load = Button()

    select_folder = Button('Select folder with pictures')

    display_folder_path = Str('<folder not selected>')

    selected_folder = '__none__'

    info_label = Str('Converter is ready.')

    # A platform-independent dialog to select a directory with images:
    dialog = DirectoryDialog()

    # If user clicks on 'Select folder with pictures':
    def _select_folder_fired(self):
        result = self.dialog.open()
        if result == OK:
            self.selected_folder = self.dialog.path
            if len(self.dialog.path) > 40:
                self.display_folder_path = '...' + self.dialog.path[-40:]
            else:
                self.display_folder_path = self.dialog.path

    # If user clicks on 'Load':
    def _load_fired(self):
        if self.selected_folder == '__none__':
            self.info_label = 'No folder has been selected.'
        else:
            # Create '.tmp' directory:
            if not os.path.exists('.tmp'):
                os.mkdir('.tmp')

            # Create string for commands:
            to_write = ''
            if self.invert:
                to_write += 'invert true\n'
            to_write += 'folder\n'
            to_write += self.selected_folder[1:] + '\n'
            to_write += 'converter\nload\n'

            # Write commands file:
            with open('.tmp/input', mode='w', encoding='utf-8') as file:
                file.write(to_write)

            self.info_label = 'Loading...'

            # Run generator with created input:
            if not os.path.exists('generator'):
                self.info_label = 'Generator executable not found. Have you built this project correctly?\n'
            os.system('./generator <.tmp/input 1>.tmp/output 2>.tmp/error')

            if not os.path.exists('.tmp/output'):
                error('Output not created')

            # Read the generator output and get the info from it:
            output_str = ''
            with open('.tmp/output', mode='r', encoding='utf-8') as file:
                output_str = file.read()
            lines = output_str.split('\n')
            imgs_loaded = int(lines[-4][7])
            output_str = ''
            for line in lines[-4-imgs_loaded:-4+1]:
                output_str += line + '\n'
            self.info_label = output_str

            # Delete temporary stuff:
            os.remove('.tmp/input')
            os.remove('.tmp/output')
            os.remove('.tmp/error')
            os.removedirs('.tmp')

    def _convert_fired(self):
        if self.selected_folder == '__none__':
            self.info_label = 'No folder has been selected.'
        else:
            self.info_label = 'Converting...'

            # Create '.tmp' directory:
            if not os.path.exists('.tmp'):
                os.mkdir('.tmp')

            # Create string for commands:
            to_write = ''
            if self.invert:
                to_write += 'invert true\n'
            to_write += 'folder\n'
            to_write += self.selected_folder[1:] + '\n'
            to_write += 'converter\nload\n'
            to_write += 'width ' + str(self.width) + '\n'
            to_write += 'convert\n'

            # Write commands file:
            with open('.tmp/input', mode='w', encoding='utf-8') as file:
                file.write(to_write)

            print('before')

            # Run generator with created input:
            if not os.path.exists('generator'):
                self.info_label = 'Generator executable not found. Have you built this project correctly?\n'
            os.system('./generator <.tmp/input 1>.tmp/output 2>.tmp/error')
            print('after')

            if not os.path.exists('.tmp/output'):
                error('Output not created')

            # Read the generator output and get the info from it:
            output_str = ''
            with open('.tmp/output', mode='r', encoding='utf-8') as file:
                output_str = file.read()
            lines = output_str.split('\n')
            k = -4
            line = lines[k]
            output_str = ''
            while 'Convert' in line:
                if 'Converted' in line:
                    output_str += line + '\n'
                k -= 1
                line = lines[k]
            self.info_label = output_str

            # Remove temporary stuff:
            os.remove('.tmp/input')
            os.remove('.tmp/output')
            os.remove('.tmp/error')
            os.removedirs('.tmp')

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
            ),
            Item('info_label', show_label=False, style='readonly')
        )
    )
