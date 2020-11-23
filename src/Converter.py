import os
from pprint import pprint
from threading import Thread
from time import sleep

from pyface.constant import OK
from pyface.directory_dialog import DirectoryDialog
from traits.api import *
from traitsui.api import *

from src.ConverterThread import ConverterThread
from src.LoaderThread import LoaderThread


class InfoLabel(HasTraits):
    label = Str()

    view = View(
        Item('label', show_label=False, style='readonly')
    )


class Converter(HasTraits):
    def __init__(self, application, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.application = application

    # Max width for the conversion:
    width = Int(0)

    convert = Button()

    load = Button()

    select_folder = Button('Select folder with pictures')

    display_folder_path = Str('<folder not selected>')

    selected_folder = '__none__'

    convert_info_label = Str('Converter is ready.')

    previous_image = Button('<')

    current_image = Str('<none>')

    next_image = Button('>')

    show_image = Button('Show Image')

    smaller_font = Button('-')

    font_size = Int(5)

    larger_font = Button('+')

    select_converted_folder = Button('Select folder with converted pictures')

    selected_converted_folder = '__none__'

    display_converted_folder_path = Str('<folder not selected>')

    shower_info_label = Str('No ascii pictures to show.')

    # A platform-independent dialog to select a directory with images:
    dialog = DirectoryDialog()
    dialog2 = DirectoryDialog()

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
            self.convert_info_label = 'No folder has been selected.'
        else:
            self.convert_info_label = 'Loading...'
            loader = LoaderThread(self)
            loader.start()

    def _convert_fired(self):
        if self.selected_folder == '__none__':
            self.convert_info_label = 'No folder has been selected.'
        else:
            self.convert_info_label = 'Converting...'
            converter = ConverterThread(self)
            converter.start()

    def _select_converted_folder_fired(self):
        result = self.dialog.open()
        if result == OK:
            self.selected_converted_folder_folder = self.dialog.path
            if len(self.dialog.path) > 40:
                self.display_converted_folder_path = '...' + self.dialog.path[-40:]
            else:
                self.display_converted_folder_path = self.dialog.path

    def _larger_font_fired(self):
        self.font_size += 1

    def _smaller_font_fired(self):
        self.font_size -= 1

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
            Item('convert_info_label', show_label=False, style='readonly'),
            VGroup(
                HGroup(
                    Item('select_converted_folder', show_label=False),
                    Item('display_converted_folder_path', show_label=False, style='readonly')
                ),
                HGroup(
                    VGroup(
                        HGroup(
                            Item('smaller_font', show_label=False),
                            Item('font_size', label='Font size:', style='readonly'),
                            Item('larger_font', show_label=False)
                        ),
                        HGroup(
                            Item('previous_image', show_label=False),
                            Item('current_image', show_label=False, style='readonly'),
                            Item('next_image', show_label=False)
                        )
                    ),
                    Item('show_image', show_label=False)
                )
            ),
            Item('shower_info_label', show_label=False, style='readonly')
        )
    )
