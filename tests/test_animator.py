from traitsui.testing.api import *
from src.Application import Application
from src.Animator import Animator

tester = UITester()
app = Application()
animator = Animator(app)


def test_change_font_size():
    with tester.create_ui(animator) as ui:
        font_editor = tester.find_by_name(ui, 'font_size')
        font_editor_slider = font_editor.locate(Slider())
        font_editor_text = font_editor.locate(Textbox())
        assert animator.font_size == 3
        font_editor_slider.perform(KeyClick('Page Down'))
        assert animator.font_size == 2
        font_editor_slider.perform(KeyClick('Page Down'))
        assert animator.font_size == 1
        font_editor_slider.perform(KeyClick('Page Down'))
        assert animator.font_size == 1
        font_editor_text.perform(KeyClick('Backspace'))
        font_editor_text.perform(KeyClick('9'))
        font_editor_text.perform(KeyClick('Enter'))
        assert animator.font_size == 9


def test_change_fps():
    with tester.create_ui(animator) as ui:
        fps_editor = tester.find_by_name(ui, 'fps')
        fps_editor_slider = fps_editor.locate(Slider())
        fps_editor_text = fps_editor.locate(Textbox())
        assert animator.fps == 30
        fps_editor_text.perform(KeyClick('Backspace'))
        fps_editor_text.perform(KeyClick('Backspace'))
        fps_editor_text.perform(KeyClick('1'))
        fps_editor_text.perform(KeyClick('Enter'))
        assert animator.fps == 1
        fps_editor_slider.perform(KeyClick('Page Down'))
        assert animator.fps == 1
