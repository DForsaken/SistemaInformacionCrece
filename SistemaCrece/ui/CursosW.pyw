#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys
import AgregarAreaW
from Curso import Ui_MainWindow

class Curso(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


    def agregarEstudianteCurso(self):
        self.hide()

    def agregarMaestroCurso(self):
        self.hide()

    def agregarCurso(self):
        self.hide()

    def agregarCausaFaltaCurso(self):
        self.hide()

    def verMaestros(self):
        self.hide()

    def verEstudiantes(self):
        self.hide()

    def verCatalogoCursos(self):
        self.hide()

    def verListaAsistencia(self):
        self.hide()

    def agregarAlumnoCurso(self):
        self.hide()



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Curso()
    myapp.show()
    sys.exit(app.exec_())
