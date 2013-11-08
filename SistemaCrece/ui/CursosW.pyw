#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys
import AgregarPersonaCursoW, AgregarCursoW, AgregarCausaFaltaW
from Cursos import Ui_MainWindow
from PyQt4.QtCore import pyqtSignal


#import AgregarAreaW, AgregarPersonaW, InicioW, AgregarDonadorW, AgregarClasificacionW, CursosW
#from Principal import Ui_MainWindow
#from PyQt4.QtCore import pyqtSignal

class Curso(QtGui.QMainWindow):

    closed = pyqtSignal()
    peticion = pyqtSignal()
    args = []
    dataTypeFlag = 0

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        if "sd" == "sd":
            print "d"

    def agregarEstudianteCurso(self):
        myapp = AgregarPersonaCursoW.AgregarPersonaCurso(self)
        myapp.closed.connect(self.show)
        myapp.show()
        self.hide()

    def agregarMaestroCurso(self):
        myapp = AgregarPersonaCursoW.AgregarPersonaCurso(self)
        myapp.closed.connect(self.show)
        myapp.show()
        self.hide()

    def agregarCurso(self):
        myapp = AgregarCursoW.AgregarCurso(self)
        myapp.closed.connect(self.show)
        myapp.show()
        self.hide()

    def agregarCausaFaltaCurso(self):
        myapp = AgregarCausaFaltaW.AgregarCausaFalta(self)
        myapp.closed.connect(self.show)
        myapp.show()
        self.hide()
    
    def agregarAlumnoCurso(self):
        myapp = AgregarPersonaCursoW.AgregarPersonaCurso(self)
        myapp.closed.connect(self.show)
        myapp.show()
        self.hide()   

    def verMaestros(self):
        self.dataTypeFlag = 1
        self.procesarPeticionVer(["verMaestros","","tabla"])
        
    def verEstudiantes(self):
        self.dataTypeFlag = 1
        self.procesarPeticionVer(["verEstudiante","","tabla"])

    def verCatalogoCursos(self):
        self.dataTypeFlag = 1
        self.procesarPeticionVer(["verCurso","","tabla"])

    def verListaAsistencia(self):
        self.dataTypeFlag = 1
        self.procesarPeticionVer(["verAsistencia","","tabla"])

    def obtenerTabla(self, res):
        print res
        rows = len(res)
        cols = len(res[0])
        self.ui.tableWidgetInfo.setRowCount(rows)
        self.ui.tableWidgetInfo.setColumnCount(cols)
        for i in range(0,rows):
            for j in range (0,cols):                    
                item = str(res[i][j])    
                item = QtGui.QTableWidgetItem(item)
                item.setFlags( QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled )
                self.ui.tableWidgetInfo.setItem(i,j,item)
        print "tabla lista"        
        
        
    
    def cambiarVistaTabla(self, res):
        print "cambiando vista"
        #self.ui.tableWidgetInfo = tablaNueva
        for row in range(0,len(res)):
            self.ui.tableWidgetInfo.insertRow(row)
            record = res[row]                 
            for column in range (0,len(record)):                        
                newitem = QtGui.QTableWidgetItem(str(record[column]))
                self.ui.tableWidgetInfo.setItem(row,column,newitem)

    def procesarPeticion(self, app):    
        if len(app.args) > 0:
            self.args = app.args[:]
            print self.peticion.emit()
            print "procesar peticion app"
            
    def procesarPeticionVer(self, args):    
        if len(args) > 0:
            self.args = args[:]
            print self.peticion.emit()
            print "procesar peticion ver"         

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Curso()
    myapp.show()
    sys.exit(app.exec_())
