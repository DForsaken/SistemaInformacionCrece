#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys
import AgregarAreaW, AgregarPersonaW, InicioW, AgregarDonadorW, AgregarClasificacionW, CursosW
from Principal import Ui_MainWindow
from PyQt4.QtCore import pyqtSignal

class Principal(QtGui.QMainWindow):

    peticion = pyqtSignal()
    args = []
    dataTypeFlag = 0
    # 0 for string
    # 1 for table
    # 2 for comobox
        

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.inicio()
       
    def inicio(self):
        inicio = InicioW.Inicio(self)
        inicio.closed.connect(self.show)
        inicio.show()
        self.hide()
        
    def agregarEmpleado(self):
        #mismo formulario que persona solo que agregar atributos faltantes en campos temp
        myapp = AgregarPersonaW.AgregarPersona(self)
        myapp.closed.connect(self.show)
        myapp.show()
        self.hide()

    def agregarArea(self):
        myapp = AgregarAreaW.AgregarArea(self)
        myapp.closed.connect(self.show)
        myapp.agregar.connect(lambda:self.procesarPeticion(myapp))
        myapp.show()
        self.hide()

    def agregarNino(self):
        myapp = AgregarPersonaW.AgregarPersona(self)
        myapp.closed.connect(self.show)
        myapp.show()
        self.hide()

    def agregarAdulto(self):
        #mismo formulario que persona solo que agregar atributos faltantes en campos temp
        myapp = AgregarPersonaW.AgregarPersona(self)
        myapp.closed.connect(self.show)
        myapp.show()
        self.hide()

    def agregarEstudiante(self):
        #mismo formulario que persona solo que agregar atributos faltantes en campos temp
        myapp = AgregarPersonaW.AgregarPersona(self)
        myapp.closed.connect(self.show)
        myapp.show()
        self.hide()
            
    def agregarDonador(self):
        myapp = AgregarDonadorW.AgregarDonador(self)
        myapp.closed.connect(self.show)
        myapp.show()
        self.hide()

    def agregarClasificacion(self):
        myapp = AgregarClasificacionW.AgregarClasificacion(self)
        myapp.closed.connect(self.show)
        myapp.show()
        self.hide() 
        
    def agregarInstitucion(self):
        myapp = AgregarDonadorW.AgregarDonador(self)
        myapp.closed.connect(self.show)
        myapp.show()
        self.hide() 

    def verEmpleado(self):
        self.dataTypeFlag = 1
        self.procesarPeticionVer(["verEmpleado","","tabla"])
        
    def verNino(self):
        self.dataTypeFlag = 1
        self.procesarPeticionVer(["verNino","","tabla"])
        
    def verAdulto(self):
        self.dataTypeFlag = 1
        self.procesarPeticionVer(["verAdulto","","tabla"])
        
    def verEstudiante(self):
        self.dataTypeFlag = 1
        self.procesarPeticionVer(["verEstudiante","","tabla"])


    def verCurso(self):
        verCurso = CursosW.Curso(self)
        verCurso.closed.connect(self.show)
        verCurso.show()
        self.hide() 
        
    def verInstitucion(self):
        self.dataTypeFlag = 1
        self.procesarPeticionVer(["verInstitucion","","tabla"])
        return None

    def verDonador(self):
        self.dataTypeFlag = 1
        self.procesarPeticionVer(["verDonador","","tabla"])

    def verArea(self):
        '''
        args -> tupla 3 elementos
        args[0] = nombre procedimiento
        args[1] = argumentos
        args[2] = tipo de retorno (tabla, string, comboBox)
        ''' 
        self.dataTypeFlag = 1  
        #self.obtenerTabla(self.procesarPeticionVer(["verArea","","tabla"]))
        self.procesarPeticionVer(["verArea","","tabla"])
        print "obtiene tabla"
        #self.cambiarVistaTabla(tabla)
        
    def obtenerTabla(self, res):
        print res
        if(res != None):
            if(len(res) != 0):
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
            else:
                print "tabla vacia"        
        else:
            print "Empty result set"
        
    
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
    



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Principal()
    myapp.show()
    sys.exit(app.exec_())
