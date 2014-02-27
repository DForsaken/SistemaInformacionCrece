#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys
import comboBoxUtilities

from PyQt4.QtCore import pyqtSignal
from AgregarDonador import Ui_Form

class AgregarDonador(QtGui.QMainWindow):

    closed = pyqtSignal()
    agregar = pyqtSignal()
    peticion = pyqtSignal()

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Sistema Crece")
        self.args = ["",[],""] 
        '''
            args -> tupla 3 elementos
            args[0] = nombre procedimiento
            args[1] = argumentos
            args[2] = tipo de retorno (tabla, string, comboBox)
        ''' 
        self.comboUtilities = comboBoxUtilities.comboBoxUtilities()
        self.comboBoxActual = None
        self.dataTypeFlag = 2
        self.args[2] = "comboBox"

    def llenarComboBox(self):
        self.comboBoxActual = self.ui.clasificacionComboBox
        self.comboUtilities.setIndex("Clasificacion")
        self.ejectuarPeticion("verClasificacion")
        self.comboBoxActual = self.ui.viaDonacionComboBox
        self.comboUtilities.setIndex("ViaDonacion")
        self.ejectuarPeticion("verViaDonacion")
       
    def ejectuarPeticion(self, proc):
        self.args[0] = proc
        self.args[1] = []
        self.peticion.emit()
        print self.args[0]
            
    def obtenerComboBox(self, res):
        self.comboUtilities.populateComboBox(self.comboBoxActual, res)

    def agregarDonador(self):
        self.args = ["",[],""]
        try:
            self.prepararArgs()
        except  ValueError:
            self.mostrarMensaje("Inserta solo valores numericos en los campos numericos !")
            return
        self.args[0] = "insertaInstitucion"
        self.args[2] = "string"
        self.dataTypeFlag = 0
        self.agregar.emit()
        self.cancelar()
        
    def prepararArgs(self):
        self.args[1].append(self.ui.clasificacionComboBox.getIdFromCurrentItem()[0])
        self.args[1].append(self.ui.viaDonacionComboBox.getIdFromCurrentItem()[0])
        self.args[1].append(float(self.ui.cantidadTxt.text()))
        self.args[1].append(str(self.ui.fechaInicioDate.text()))
        self.args[1].append(str(self.ui.fechaFinDate.text()))
        self.args[1].append(str(self.ui.nombreTxt.text()))
        self.args[1].append(str(self.ui.direccionTxt.text()))
        self.args[1].append(int(self.ui.telefonoTxt.text()))
        self.args[1].append(str(self.ui.emailTxt.text()))
        #status persona
        self.args[1].append(1)
        #ruta carpeta
        self.args[1].append("")

    def mostrarMensaje(self, mensaje):    
        QtGui.QMessageBox.critical(self, 'Error !', mensaje, QtGui.QMessageBox.Ok)
        
    def cancelar(self):
        self.closed.emit()
        self.close()

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = AgregarDonador()
    myapp.show()
    sys.exit(app.exec_())