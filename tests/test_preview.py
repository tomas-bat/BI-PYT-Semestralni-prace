from traitsui.testing.api import *

from src.Application import Application
from src.Preview import Preview

app = Application()
preview = Preview(app)
tester = UITester()


