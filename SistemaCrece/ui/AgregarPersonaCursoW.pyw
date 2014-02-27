#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys, comboBoxUtilities

from PyQt4.QtCore import pyqtSignal
from AgregarPersonaCurso import Ui_Form


class AgregarPersonaCurso(QtGui.QMainWindow):

    closed = pyqtSignal()

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Sistema Crece")
        self.comboBoxActual = None
        self.dataTypeFlag = 2
        # 0 for string
        # 1 for table
        # 2 for combobox
        self.args = ["",[],""] 
        '''
            args -> tupla 3 elementos
            args[0] = nombre procedimiento
            args[1] = argumentos
            args[2] = tipo de retorno (tabla, string, comboBox)
        ''' 
        self.comboUtilities = comboBoxUtilities.comboBoxUtilities()

    def llenarComboBox(self):
        self.args[2] = "comboBox"
        self.comboBoxActual = self.ui
        self.comboUtilities.setIndex("Colonia")
        self.ejectuarPeticion("verColonia")

    def agregarPersonaCurso(self):
        self.cancelar()

    def cancelar(self):
        self.close()

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = AgregarPersonaCurso()
    myapp.show()
    sys.exit(app.exec_())