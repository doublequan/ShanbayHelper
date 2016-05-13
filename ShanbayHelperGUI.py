__author__ = 'Administrator'

# coding utf-8
from PyQt4 import QtGui
from PyQt4 import QtCore
from ShanbayHelperBackend import ShanbayHelperBackend
import os
import time

class ShanbayHelperGUI(QtGui.QWidget):

    def __init__(self):
        super(ShanbayHelperGUI, self).__init__()

        self.initUI()
        self.loadCache()
        self.setConnections()
        self.updateWordListState()
        self.backend = ShanbayHelperBackend(self)


    def initUI(self):
        self.setFont(QtGui.QFont('OldEnglish', 18, 100))
        self.setWindowTitle('Helper for Shanbay.com')
        self.resize(400, 600)
        self.setWindowIcon(QtGui.QIcon('images/carnegie-mellon-university-playfair.jpg'))

        username = QtGui.QLabel('UserName :')
        password = QtGui.QLabel('Password :')

        self.usernameEdit = QtGui.QLineEdit()
        self.passwordEdit = QtGui.QLineEdit()

        #self.loginButton = QtGui.QPushButton('LogIn')
        #self.registerButton = QtGui.QPushButton('Register')

        self.loginState = QtGui.QLabel('Please Type in the Username and Password ^_^');

        self.wordlistEdit = QtGui.QTextEdit()

        self.wordlistState = QtGui.QLabel('0 words now')

        self.clearButton = QtGui.QPushButton('Clear All')
        self.clearButton.setMinimumHeight(40)
        self.clearButton.setMaximumWidth(300)

        self.submitButton = QtGui.QPushButton('Submit All')
        self.submitButton.setMinimumHeight(80)
        self.submitButton.setMaximumWidth(300)

        grid = QtGui.QGridLayout()
        grid.setSpacing(20)
        grid.setMargin(50)

        grid.addWidget(username, 0, 0)
        grid.addWidget(self.usernameEdit, 0, 1, 1, 1)
        grid.addWidget(password, 1, 0)
        grid.addWidget(self.passwordEdit, 1, 1, 1, 1)

        #grid.addWidget(self.loginButton, 2, 0)
        #grid.addWidget(self.registerButton, 2, 1)
        grid.addWidget(self.loginState, 3, 0, 1, 2)

        grid.addWidget(self.wordlistEdit, 5, 0, 4, 1)
        grid.addWidget(self.wordlistState, 5, 1)
        grid.addWidget(self.clearButton, 6, 1)
        grid.addWidget(self.submitButton, 7, 1, 2, 1)

        self.setLayout(grid)

    def setConnections(self):
        self.connect(self.wordlistEdit, QtCore.SIGNAL('textChanged()'),
                     self.updateWordListState)
        self.connect(self.clearButton, QtCore.SIGNAL('clicked()'),
                     self.wordlistEdit, QtCore.SLOT('clear()'))
        self.connect(self.submitButton, QtCore.SIGNAL('clicked()'),
                     self.execute)

    def updateWordListState(self):
        '''
        This funcation will be called every time wordlistEdit changed
        :return:
        '''
        self.wordList = self.wordlistEdit.document().toPlainText().split('\n')
        self.wordList = [x for x in self.wordList if len(x) != 0]
        #print(wordList)
        self.wordlistState.setText(str(len(self.wordList)) + ' words now')


    def execute(self):
        #self.disableWidget()

        self.saveCache()

        self.backend.openChrome()
        usr = self.usernameEdit.text()
        pw = self.passwordEdit.text()
        if self.backend.login(usr, pw):
            self.wordlistState.setText('Login Successfully')
            self.backend.addWordList(self.wordList)
            self.wordlistState.setText('Added ' + str(len(self.wordList)) + ' Words')
        self.backend.exitChrome()

        #self.enableWidget()

    def disableWidget(self):
        self.usernameEdit.setDisabled(True)
        self.passwordEdit.setDisabled(True)
        self.wordlistEdit.setDisabled(True)
        self.clearButton.setDisabled(True)
        self.submitButton.setDisabled(True)
        pass

    def enableWidget(self):
        self.usernameEdit.setDisabled(False)
        self.passwordEdit.setDisabled(False)
        self.wordlistEdit.setDisabled(False)
        self.clearButton.setDisabled(False)
        self.submitButton.setDisabled(False)
        pass

    def log(self, string):
        abspath = os.path.abspath('.')
        logpath = abspath + '\\log'
        if not os.path.isdir(logpath):
            os.mkdir(logpath)

        date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        t = time.strftime('%H:%M', time.localtime(time.time()))
        with open(logpath + '\\' + date, 'a') as f:
            f.write(t + '  ' + string + '\n')

    def loadCache(self):
        abspath = os.path.abspath('.')
        cachepath = path = abspath + '\\log\\cache'
        if not os.path.exists(cachepath):
            return

        with open(cachepath, 'r') as f:
            usr = f.readline().replace('\n', '')
            pw = f.readline().replace('\n', '')
            self.usernameEdit.setText(usr)
            self.passwordEdit.setText(pw)

    def saveCache(self):
        abspath = os.path.abspath('.')
        logpath = abspath + '\\log'
        if not os.path.isdir(logpath):
            os.mkdir(logpath)

        cachepath = path = abspath + '\\log\\cache'
        with open(cachepath, 'w') as f:
            usr = self.usernameEdit.text()
            pw = self.passwordEdit.text()
            f.write(usr + '\n' + pw + '\n')