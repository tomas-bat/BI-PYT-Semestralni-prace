from traitsui.api import *
from traits.api import *
import time

from src.AnimationThread import AnimationThread


class AnimationShower(HasTraits):
    def __init__(self, ascii, fps, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ascii = ascii
        self.fps = fps
        self.ascii_label = self.ascii[0]

    ascii_label = Str()

    play = Button('Play')

    def _play_fired(self):
        thread = AnimationThread(self)
        thread.start()
