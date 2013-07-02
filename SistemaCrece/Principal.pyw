#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys
import AgregarAreaW
from Principal import Ui_MainWindow

class Principal(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def agregarEmpleado(self):
        self.close()

    def agregarArea(self):
        myapp = AgregarAreaW.Cursos(self)
        myapp.closed.connect(self.show)
        myapp.show()
        self.hide()

    def agregarNino(self):
        self.close()

    def agregarAdulto(self):
        self.close()

    def agregarEstudiante(self):
        self.hide()

    def verEmpleado(self):
        self.hide()

    def verNino(self):
        self.hide()

    def verAdulto(self):
        self.hide()

    def verEstudiante(self):
        self.hide()

    def verCurso(self):
        self.hide()

    def agregarInstitucion(self):
        self.hide()

    def verInstitucion(self):
        self.hide()

    def agregarDonador(self):
        self.hide()

    def agregarClasificacion(self):
        self.hide()

    def verDonador(self):
        self.hide()

    def verArea(self):
        self.hide()



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Principal()
    myapp.show()
    sys.exit(app.exec_())
