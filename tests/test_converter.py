import os
import time

from traitsui.testing.api import *

from src.Application import Application
from src.Converter import Converter

app = Application()
converter = Converter(app)
tester = UITester()


def test_load_1():
    with tester.create_ui(converter) as ui:
        display_folder_label = tester.find_by_name(ui, 'display_folder_path')
        info_label = tester.find_by_name(ui, 'convert_info_label')
        load_button = tester.find_by_name(ui, 'load')
        if display_folder_label == '<folder not selected>':
            load_button.perform(MouseClick())
            assert info_label == 'No folder has been selected.'


def test_convert_1():
    with tester.create_ui(converter) as ui:
        display_folder_label = tester.find_by_name(ui, 'display_folder_path')
        info_label = tester.find_by_name(ui, 'convert_info_label')
        convert_button = tester.find_by_name(ui, 'convert')
        if display_folder_label == '<folder not selected>':
            convert_button.perform(MouseClick())
            assert info_label == 'No folder has been selected.'


def test_convert_2():
    with tester.create_ui(converter) as ui:
        converter.selected_folder = os.path.join(

            os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'examples')
        convert_button = tester.find_by_name(ui, 'convert')
        width_field = tester.find_by_name(ui, 'width')
        width_field.perform(KeySequence('300'))
        assert converter.width == 300
        convert_button.perform(MouseClick())
        while converter.in_progress:
            time.sleep(1)
        assert os.path.exists('examples/converted')
        assert os.path.exists('examples/converted/cpp.png.ascii')
        assert os.path.exists('examples/converted/Linux.jpg.ascii')
        assert os.path.exists('examples/converted/Saturn.png.ascii')
