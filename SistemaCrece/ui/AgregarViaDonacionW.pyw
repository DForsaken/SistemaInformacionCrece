#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys

from PyQt4.QtCore import pyqtSignal
from AgregarViaDonacion import Ui_Form

class AgregarViaDonacion(QtGui.QMainWindow):

    closed = pyqtSignal()
    agregar = pyqtSignal()

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Sistema Crece")
        self.dataTypeFlag = "string"
        self.args = ["insertaViaDonacion",[],""]

    def agregarViaDonacion(self):
        self.args[1].append(str(self.ui.viaDonacionTxt.text()))
        print self.ui.viaDonacionTxt.text(), " -> insertaViaDonacion"
        self.agregar.emit()
        self.cancelar()

    def cancelar(self):
        self.close()

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = AgregarViaDonacion()
    myapp.show()
    sys.exit(app.exec_())