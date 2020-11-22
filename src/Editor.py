from traits.api import *
from traitsui.api import *


class Editor(HasTraits):
    def __init__(self, application, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.application = application
