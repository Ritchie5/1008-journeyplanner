import sys
from windows import *

winWidth = 1080
winHeight = 720
comboWidth = 400
comboHeight = 40
comboX = (winWidth - comboWidth) / 2
comboY = (winHeight - comboHeight) / 8
testarr = ["Choa Chu Kang", "Boon Lay", "Changi"]


def test():
    pass

class win:
    def __init__(self):
        self.win = newWindow("Journey Planner", winWidth, winHeight)
        self.ui = window()
        self.ui.setupUI(self.win)

    def show(self):
        self.win.win.show()


application = newApp()
win = win()
win.show()
sys.exit(application.app.exec_())
