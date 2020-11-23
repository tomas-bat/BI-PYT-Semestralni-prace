from traits.api import *
from traitsui.api import *


class Show(HasTraits):
    def __init__(self, ascii, font_size, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ascii = ascii
        self.style_sheet = '*{font-size:' + str(font_size) + 'px; font-family:"Menlo"}'

    ascii = Str()


class MainWindow(HasTraits):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        str = ''
        with open('/Users/tom/Desktop/converted/Eliška.png.ascii', mode='r+', encoding='utf-8') as f:
            str = f.read()
        self.ascii = str

    ascii = Str()

    font_size = Int(5)

    smaller = Button()

    def _smaller_fired(self):
        self.font_size -= 1

    bigger = Button()

    def _bigger_fired(self):
        self.font_size += 1

    show = Button()

    def _show_fired(self):
        shower = Show(self.ascii, self.font_size)
        style_sheet = '*{font-size:' + str(self.font_size) + 'px; font-family:"Menlo"}'

        new_view = View(
            Item('ascii', style='readonly', show_label=False, style_sheet=style_sheet)
        )
        shower.configure_traits(view=new_view)

    view = View(
        VGroup(
            HGroup(
                Item('smaller', show_label=False),
                Item('font_size', show_label=False, style='readonly'),
                Item('bigger', show_label=False)
            ),
            Item('show', show_label=False)
        ),
        resizable=True,
        title='Test'
    )


if __name__ == '__main__':
    mainWin = MainWindow()
    mainWin.configure_traits()


