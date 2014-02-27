#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys

from PyQt4.QtCore import pyqtSignal
from AgregarArea import Ui_Form

class AgregarArea(QtGui.QMainWindow):

    closed = pyqtSignal()
    agregar = pyqtSignal()

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.setWindowTitle("Sistema Crece")
        self.ui.setupUi(self)
        self.dataTypeFlag = "string"
        self.args = ["insertaArea",[],""]


    def agregarArea(self):
        self.args[1].append(str(self.ui.areaTxt.text()))
        print self.ui.areaTxt.text(), " -> insertaArea"
        self.agregar.emit()
        self.cancelar()

    def cancelar(self):
        self.close()

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = AgregarArea()
    myapp.show()
    sys.exit(app.exec_())