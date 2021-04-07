import csv
import webbrowser
from widgets import *
from Backtracking import Backtracking
from Dijkstra import Dijkstra
from graph import Graph

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
    __tableWidth = 250
    __tableHeight = 500
    __radioWidth = 150
    __radioHeight = 40

    #Widget Coordinates
    __logoX = (__winWidth - __comboWidth) / 2
    __logoY = (__winHeight - __comboHeight) / 4
    __comboX = __logoX
    __comboY = __logoY + 100
    __labelX = __comboX - 150
    __labelY = __comboY
    __buttonX = __comboX
    __buttonY = __comboY + 100
    __tableX = (__winWidth - __tableWidth) / 2
    __tableY = 100
    __radioX = (__comboX + __comboWidth) + 20
    __radioY = __comboY

    tag = "MRT"

    #Button functions
    def dijkClicked(self):
        startLoc = self.startCombo.combo.currentText()
        destLoc = self.destCombo.combo.currentText()
        if startLoc and destLoc in self.locations:
            # Dijkstra
            temp = Dijkstra(self.graph, startLoc)
            dijkPath = temp.find_path(destLoc)
            self.dijkTable.addRow(len(dijkPath[2:]))
            self.dijkTable.addCol(1)
            self.dijkTable.addData(dijkPath[2:], 0)
            self.stackWidget.setCurrentPage(self.dijkPage)
        else:
            msgBox = newMessageBox("Error!", "Invalid input! Please check again!", "winIcon.PNG")

    def backtrackClicked(self):
        startLoc = self.startCombo.combo.currentText()
        destLoc = self.destCombo.combo.currentText()
        if startLoc and destLoc in self.locations:
                back_tracker = Backtracking()
                # BackTracking: Finding all path Algo
                pathAll = back_tracker.find_all_path(self.graph.adjList, startLoc, destLoc, 0, 0)
                i = j = k = rowCount = 0
                while k <= (len(pathAll)-1):
                    if rowCount < len(pathAll[k][2:]):
                        rowCount = len(pathAll[k][2:])
                    k += 1

                self.backTrackTableAll.addRow(rowCount)
                self.backTrackTableAll.addCol(len(pathAll))
                while i <= (len(pathAll) - 1):
                    self.backTrackTableAll.addData(pathAll[i][2:], j)
                    i += 1
                    j += 1

                # BackTracking: Finding shortest path Algo
                pathShort = back_tracker.find_shortest_path(self.graph.adjList, startLoc, destLoc, 0, 0)
                self.backTrackTableShort.addRow(len(pathShort[2:]))
                self.backTrackTableShort.addCol(1)
                self.backTrackTableShort.addData(pathShort[2:], 0)
                self.stackWidget.setCurrentPage(self.backTrackPage)
        else:
            msgBox = newMessageBox("Error!", "Invalid input! Please check again!", "winIcon.PNG")

    def backClicked(self):
        self.stackWidget.setCurrentPage(self.mainPage)

    #Call function to setup UI
    def setupUI(self, window):
        window.setWindowIcon("winIcon.PNG")
        self.cenWidget = QtWidgets.QWidget(window.win)
        window.win.setCentralWidget(self.cenWidget)
        self.stackWidget = newStackWidget(self.cenWidget, 0, 0, self.__winWidth, self.__winHeight)

        self.graph = Graph("graph.csv", self.tag)

        self.mainWin()
        self.dijkWin()
        self.backTrackWin()
        self.stackWidget.setCurrentPage(self.mainPage)

    #Call function to setup main window
    def mainWin(self):
        self.mainPage = newWidgetPage()
        self.locations = self.getLocation("graph.csv")
        self.mainlogo = newLabel(self.mainPage.page, self.__logoX, self.__logoY, self.__logoWidth, self.__logoHeight, "", "mainLogo.PNG")
        self.startCombo = newComboBox(self.mainPage.page, self.__comboX, self.__comboY, self.__comboWidth, self.__comboHeight, "Ariel", 12)
        self.startCombo.combo.addItems(self.locations)
        self.destCombo = newComboBox(self.mainPage.page, self.__comboX, self.__comboY+50, self.__comboWidth, self.__comboHeight, "Ariel", 12)
        self.destCombo.combo.addItems(self.locations)
        self.startLabel = newLabel(self.mainPage.page, self.__labelX, self.__labelY, self.__labelWidth, self.__labelHeight, "Select Starting Point:", "", "Ariel", 12)
        self.destLabel = newLabel(self.mainPage.page, self.__labelX+16, self.__labelY+50, self.__labelWidth, self.__labelHeight, "Select Destination:", "", "Ariel", 12)
        self.dijkButton = newPushButton(self.mainPage.page, self.__buttonX, self.__buttonY, self.__buttonWidth, self.__buttonHeight, self.dijkClicked, "Use Dijkstra", "Ariel", 12)
        self.backtrackButton = newPushButton(self.mainPage.page, self.__buttonX+250, self.__buttonY, self.__buttonWidth, self.__buttonHeight, self.backtrackClicked, "Use Backtrack", "Ariel", 12)
        self.mrtRadio = newRadioButton(self.mainPage.page, self.__radioX, self.__radioY, self.__radioWidth, self.__radioHeight, "MRT Only", "Ariel", 12)
        self.busRadio = newRadioButton(self.mainPage.page, self.__radioX, self.__radioY+50, self.__radioWidth, self.__radioHeight, "Bus Only", "Ariel", 12)
        self.stackWidget.addPage(self.mainPage.page)

    def dijkWin(self):
        self.dijkPage = newWidgetPage()
        self.backButton = newPushButton(self.dijkPage.page, self.__buttonX+250, self.__buttonY+250, self.__buttonWidth, self.__buttonHeight, self.backClicked, "Back", "Ariel", 12)
        self.dijkLinkButton = newPushButton(self.dijkPage.page, self.__buttonX, self.__buttonY+250, self.__buttonWidth, self.__buttonHeight, self.openLink, "Check Traffic", "Ariel", 12)
        self.dijkTable = newTable(self.dijkPage.page, self.__tableWidth+165, self.__tableY, self.__tableWidth, self.__tableHeight)
        self.stackWidget.addPage(self.dijkPage.page)

    def backTrackWin(self):
        self.backTrackPage = newWidgetPage()
        self.backButton = newPushButton(self.backTrackPage.page, self.__buttonX+358, self.__buttonY+250, self.__buttonWidth, self.__buttonHeight, self.backClicked, "Back", "Ariel", 12)
        self.btLinkButton = newPushButton(self.backTrackPage.page, self.__buttonX-107, self.__buttonY+250, self.__buttonWidth, self.__buttonHeight, self.openLink, "Check Traffic", "Ariel", 12)
        self.backTrackTableAll = newTable(self.backTrackPage.page, self.__tableX-400, self.__tableY, self.__tableWidth+500, self.__tableHeight)
        self.backTrackTableShort = newTable(self.backTrackPage.page, self.__tableX+380, self.__tableY, self.__tableWidth, self.__tableHeight)
        self.allPathImage = newLabel(self.backTrackPage.page, 0, 0, self.__labelWidth, self.__labelHeight, "", "allPath.png")
        self.stackWidget.addPage(self.backTrackPage.page)

    def getLocation(self, file):
        # filename = open("graph.csv", "r")
        # file = csv.DictReader(filename)
        # tempArr = []
        # locArr = []
        # for col in file:
        #     tempArr.append(col["Pasir ris"])
        # locArr.append("Pasir ris")
        # for x in tempArr:
        #     if x not in locArr:
        #         locArr.append(x)
        # return locArr
        g = Graph("graph.csv", self.tag)
        return g.adjList

    def openLink(self):
        webbrowser.open_new("https://www.tomtom.com/en_gb/traffic-index/singapore-traffic/")