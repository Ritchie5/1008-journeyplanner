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
    __labelX = __comboX - 150
    __labelY = __comboY
    __buttonX = __comboX
    __buttonY = __comboY + 100


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
        self.startLabel = newLabel(self.mainPage.page, self.__labelX, self.__labelY, self.__labelWidth, self.__labelHeight, "Select Starting Point:", "", "Ariel", 12)
        self.destLabel = newLabel(self.mainPage.page, self.__labelX+16, self.__labelY+50, self.__labelWidth, self.__labelHeight, "Select Destination:", "", "Ariel", 12)
        self.dijkButton = newPushButton(self.mainPage.page, self.__buttonX, self.__buttonY, self.__buttonWidth, self.__buttonHeight, self.dijkClicked, "Use Dijkstra", "Ariel", 12)
        self.backtrackButton = newPushButton(self.mainPage.page, self.__buttonX+250, self.__buttonY, self.__buttonWidth, self.__buttonHeight, self.backtrackClicked, "Use Backtrack", "Ariel", 12)
        self.stackWidget.addPage(self.mainPage.page)

    def dijkClicked(self):
        pass

    def backtrackClicked(self):
        pass

    def getLocation(self, file):
        filename = open("graph.csv", "r")
        file = csv.DictReader(filename)
        tempArr = []
        locArr = []
        for col in file:
            tempArr.append(col["Pasir ris"])
        locArr.append("Pasir ris")
        for x in tempArr:
            if x not in locArr:
                locArr.append(x)
        return locArr