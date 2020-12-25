from time import sleep
from random import randrange
from threading import Thread


class AnimationThread(Thread):
    def __init__(self, shower):
        super().__init__()
        self.shower = shower

    def run(self):
        for frame in self.shower.ascii:
            self.shower.ascii_label = frame
            sleep(1/self.shower.fps)
