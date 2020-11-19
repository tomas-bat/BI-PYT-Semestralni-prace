from src import Application
from traits.api import *

if __name__ == '__main__':
    app = Application.Application()
    app.configure_traits(kind='modal')
