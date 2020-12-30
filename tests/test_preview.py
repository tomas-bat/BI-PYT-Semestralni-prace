from traitsui.testing.api import *

from src.Application import Application
from src.Preview import Preview

app = Application()
preview = Preview(app)
tester = UITester()


def test_font_size():
    with tester.create_ui(preview) as ui:
        font_editor = tester.find_by_name(ui, 'font_size')
        font_editor_slider = font_editor.locate(Slider())
        font_editor_text = font_editor.locate(Textbox())
        assert preview.font_size == 3
        font_editor_text.perform(KeyClick('Backspace'))
        font_editor_text.perform(KeyClick('5'))
        font_editor_text.perform(KeyClick('Enter'))
        assert preview.font_size == 5
        font_editor_slider.perform(KeyClick('Page Up'))
        assert preview.font_size == 6
