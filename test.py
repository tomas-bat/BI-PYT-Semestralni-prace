from traits.api import *
from traitsui.api import *


class Window(HasTraits):
    value = str()
    do_something = Button()

    def _do_something_fired(self):
        self.value = str()
        print('yello')

    view = View('value', Item('do_something', show_label=False))


if __name__ == '__main__':
    window = Window()
    window.configure_traits()

