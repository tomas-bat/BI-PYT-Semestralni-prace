from traits.api import *
from traitsui.api import *

from test_othefile import Sub


class Main(HasTraits):
    sub = Instance(Sub)

    invert = Bool()

    button = Button('Change')

    def _button_fired(self):
        self.invert = not self.invert

    def _sub_default(self):
        return Sub(self)

    view = View(
        VGroup(
            Item('invert', show_label=False, style='readonly'),
            Item('button', show_label=False),
            Item('sub', show_label=False, style='custom', dock='tab'),
            layout='tabbed'
        )
    )


if __name__ == '__main__':
    main = Main()
    main.configure_traits()


