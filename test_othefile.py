from traits.api import *
from traitsui.api import *


class Sub(HasTraits):
    def __init__(self, main_class, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.main_class = main_class

    invert_copy = Bool()

    get = Button('Get')

    def _get_fired(self):
        self.invert_copy = self.main_class.invert

    view = View(
        VGroup(
            Item('invert_copy', style='readonly'),
            Item('get', show_label=False)
        )
    )
