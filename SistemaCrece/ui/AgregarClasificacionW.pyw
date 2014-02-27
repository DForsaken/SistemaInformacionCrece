#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys

from PyQt4.QtCore import pyqtSignal
from AgregarClasificacion import Ui_Form

class AgregarClasificacion(QtGui.QMainWindow):

    closed = pyqtSignal()
    agregar = pyqtSignal()
    args = ["insertaClasificacion",[],""]

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Sistema Crece")
        self.dataTypeFlag = "string"

    def agregarClasificacion(self):
        self.args[1].append(str(self.ui.clasificacionTxt.text()))
        print self.ui.clasificacionTxt.text(), " -> insertaClasificacion"
        self.agregar.emit()
        self.cancelar()

    def cancelar(self):
        self.close()

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = AgregarClasificacion()
    myapp.show()
    sys.exit(app.exec_())