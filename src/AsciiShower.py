from traits.api import *


class AsciiShower(HasTraits):
    def __init__(self, ascii, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ascii = ascii

    ascii = Str()
