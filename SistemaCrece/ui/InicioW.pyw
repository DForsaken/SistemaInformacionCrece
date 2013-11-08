#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys

from PyQt4.QtCore import pyqtSignal
from Inicio import Ui_Form
import PrincipalW

class Inicio(QtGui.QMainWindow):

    closed = pyqtSignal()

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def ingresar(self):
        self.close()       
        
    def closeEvent(self, event):
        self.closed.emit()
        event.accept()
        

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Inicio()
    myapp.show()
    sys.exit(app.exec_())