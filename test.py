import sys
from gui import *

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
        self.page1 = newWidgetPage()
        self.cenWidget = QtWidgets.QWidget(self.win.window)
        self.win.window.setCentralWidget(self.cenWidget)
        self.stack = newStackWidget(self.cenWidget, 0,0, winWidth,winHeight)
        self.startCombo = newComboBox(self.page1.page, comboX, comboY, comboWidth, comboHeight)
        self.startCombo.combo.addItems(testarr)
        self.destCombo = newComboBox(self.page1.page, comboX, comboY+50, comboWidth, comboHeight)
        self.destCombo.combo.addItems(testarr)
        self.stack.addPage(self.page1.page)
        self.stack.setCurrentPage(self.page1)

    def show(self):
        self.win.window.show()


application = newApp()
win = win()
win.show()
sys.exit(application.app.exec_())
