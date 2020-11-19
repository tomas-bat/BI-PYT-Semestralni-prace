from traits.api import *
from traitsui.api import *


class Converter(HasTraits):
    width = Int()
    convert = Button()
    load = Button()

    view = View(
        HGroup(
            Item("width"),
            Item("load"),
            Item("convert")
        )
    )