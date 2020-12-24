import os
from src.Application import Application
from traitsui.message import *

if __name__ == '__main__':
    app = Application()
    if not os.path.exists('generator'):
        message('Generator executable not found.\nUse get_generator.sh', title='Error')
        exit(1)
    app.configure_traits()
