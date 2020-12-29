import os

from traitsui.testing.api import *

from src.Application import Application

app = Application()
tester = UITester()


def test_installed_properly():
    if not os.path.exists('generator'):
        assert False


def test_change_inversion():
    with tester.create_ui(app) as ui:
        invert = tester.find_by_name(ui, 'invert')
        assert not app.invert
        invert.perform(MouseClick())
        assert app.invert
