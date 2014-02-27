#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys, comboBoxUtilities
from PyQt4.QtCore import pyqtSignal
from AgregarEscuela import Ui_Form

class AgregarEscuela(QtGui.QMainWindow):

    closed = pyqtSignal()
    agregar = pyqtSignal()
    peticion = pyqtSignal()
   

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Sistema Crece")
        self.comboUtilities = comboBoxUtilities.comboBoxUtilities()
        self.comboBoxActual = None
        self.dataTypeFlag = 2
        self.args = ["",[],""]
        self.args[2] = "comboBox" 
        
        '''
            args -> tupla 3 elementos
            args[0] = nombre procedimiento
            args[1] = argumentos
            args[2] = tipo de retorno (tabla, string, comboBox)
        ''' 


    def llenarComboBox(self):
        self.comboBoxActual = self.ui.ColoniaComboBox
        self.comboUtilities.setIndex("Colonia")
        self.ejectuarPeticion("verColonia")
       
    def ejectuarPeticion(self, proc):
        self.args[0] = proc
        self.args[1] = []
        self.peticion.emit()
        print self.args[0]
            
    def obtenerComboBox(self, res):
        self.comboUtilities.populateComboBox(self.comboBoxActual, res)

    def agregarEscuela(self):
        self.args = ["",[],""]
        try:
            self.prepararArgs()
        except  ValueError:
            self.mostrarMensaje("Inserta solo valores numericos en los campos numericos !")
            return
        self.args[0] = "insertaEscuela"
        self.args[2] = "string"
        self.dataTypeFlag = 0
        self.agregar.emit()
        self.cancelar()

    def prepararArgs(self):
        self.args[1].append(str(self.ui.nombreTxt.text()))
        self.args[1].append(str(self.ui.domicilioTxt.text()))
        self.args[1].append(str(self.ui.ColoniaComboBox.getIdFromCurrentItem()[0]))
        self.args[1].append(int(self.ui.codigoPostalTxt.text()))
        self.args[1].append(int(self.ui.telefonoTxt.text()))

    def cancelar(self):
        self.close()

    def mostrarMensaje(self, mensaje):    
        QtGui.QMessageBox.critical(self, 'Error !', mensaje, QtGui.QMessageBox.Ok)

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = AgregarEscuela()
    myapp.show()
    sys.exit(app.exec_())