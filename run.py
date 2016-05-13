__author__ = 'Administrator'

import sys
from ShanbayHelperGUI import ShanbayHelperGUI
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)
ex = ShanbayHelperGUI()
ex.show()
sys.exit(app.exec_())