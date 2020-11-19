from traits.api import *
from traitsui.api import *


class FileDialog(Handler):
    filename = File
    open = Button('Select directory')

    view = View(
        Group(
            Item("open", editor=FileEditor())
        )
    )