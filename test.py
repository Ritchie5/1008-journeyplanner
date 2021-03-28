import sys
from gui import *

winWidth = 1080
winHeight = 720
testarr = ["Choa Chu Kang", "Boon Lay", "Changi"]


def test():
    pass

class win:
    def __init__(self):
        self.win = newWindow("Journey Planner", winWidth, winHeight)
        self.page1 = newWidgetPage()
        self.cenWidget = QtWidgets.QWidget(self.win.window)
        self.win.window.setCentralWidget(self.cenWidget)
        self.stack = newStackWidget(self.cenWidget, 0,0, winWidth,winHeight)
        self.combo = newComboBox(self.page1.page, 0,0, 400, 40)
        self.combo.combo.addItems(testarr)
        self.stack.addPage(self.page1.page)
        self.stack.setCurrentPage(self.page1)

    def show(self):
        self.win.window.show()


application = newApp()
win = win()
win.show()
sys.exit(application.app.exec_())
