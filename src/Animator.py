from traits.api import *
from traitsui.api import *


class Animator(HasTraits):
    def __init__(self, application, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.application = application

    test = Button('Test')

    def _test_fired(self):
        print('test fired, inver in animator is:', self.application.invert)

    view = View(
        Item('test', show_label=False)
    )
