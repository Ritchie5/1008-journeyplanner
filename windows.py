import csv
from widgets import *

class window:

    #Widget Dimensions
    __winWidth = 1080
    __winHeight = 720
    __logoWidth = 400
    __logoHeight = 90
    __buttonWidth = 150
    __buttonHeight = 80
    __textWidth = 400
    __textHeight = 40
    __labelWidth = 150
    __labelHeight = 40
    __comboWidth = 400
    __comboHeight = 40

    __logoX = (__winWidth - __comboWidth) / 2
    __logoY = (__winHeight - __comboHeight) / 4
    __comboX = __logoX
    __comboY = __logoY + 100


    def setupUI(self, window):
        window.setWindowIcon("winIcon.PNG")
        self.cenWidget = QtWidgets.QWidget(window.win)
        window.win.setCentralWidget(self.cenWidget)
        self.stackWidget = newStackWidget(self.cenWidget, 0, 0, self.__winWidth, self.__winHeight)

        self.mainWin()
        self.stackWidget.setCurrentPage(self.mainPage)

    def mainWin(self):
        self.mainPage = newWidgetPage()
        locations = self.getLocation("graph.csv")
        self.mainlogo = newLabel(self.mainPage.page, self.__logoX, self.__logoY, self.__logoWidth, self.__logoHeight, "", "mainLogo.PNG")
        self.startCombo = newComboBox(self.mainPage.page, self.__comboX, self.__comboY, self.__comboWidth, self.__comboHeight)
        self.startCombo.combo.addItems(locations)
        self.destCombo = newComboBox(self.mainPage.page, self.__comboX, self.__comboY+50, self.__comboWidth, self.__comboHeight)
        self.destCombo.combo.addItems(locations)
        self.stackWidget.addPage(self.mainPage.page)

    def getLocation(self, file):
        locarr = []
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                loc = row[1]
                for x in loc:
                    if x not in locarr:
                        locarr.append(x)
        return locarr