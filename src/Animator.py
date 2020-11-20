from traits.api import *
from traitsui.api import *


class Animator(HasTraits):
    def __init__(self, invert, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.invert = invert
