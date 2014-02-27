#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys, comboBoxUtilities

from PyQt4.QtCore import pyqtSignal
from AgregarCurso import Ui_Form

class AgregarCurso(QtGui.QMainWindow):

    agregar = pyqtSignal()
    peticion = pyqtSignal()
    closed = pyqtSignal()

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.comboUtilities = comboBoxUtilities.comboBoxUtilities()
        self.setWindowTitle("Sistema Crece")
        self.comboBoxActual = None
        self.dataTypeFlag = 2 
        # 0 for string
        # 1 for table
        # 2 for combobox
        self.args = ["",[],""]
        self.args[2] = "comboBox" 
        '''
            args -> tupla 3 elementos
            args[0] = nombre procedimiento
            args[1] = argumentos
            args[2] = tipo de retorno (tabla, string, comboBox)
        ''' 
            
    def llenarComboBox(self):
        self.comboBoxActual = self.ui.coloniaComboBox
        self.comboUtilities.setIndex("Colonia")
        self.ejectuarPeticion("verColonia")
        self.comboBoxActual = self.ui.areaComboBox
        self.comboUtilities.setIndex("ViaArea")
        self.ejectuarPeticion("verArea")
       
    def ejectuarPeticion(self, proc):
        self.args[0] = proc
        self.args[1] = []
        self.peticion.emit()
        print self.args[0]
            
    def obtenerComboBox(self, res):
        self.comboUtilities.populateComboBox(self.comboBoxActual, res)
        
    def agregarCurso(self):
        self.prepararArgs()
        self.args[0] = "insertaCurso"
        self.args[2] = "string"
        self.dataTypeFlag = 0
        self.agregar.emit()    
        
    def prepararArgs(self):
        self.args[1].append(self.ui.nombreTxt.text())
        self.args[1].append(self.ui.areaComboBox.getIdFromCurrentItem()[0])
        self.args[1].append(self.ui.enfoqueTxt.toPlainText())
        self.args[1].append(self.ui.fechaInicioDate.text()) 
        self.args[1].append(self.ui.fechaFinDate.text())
        #ruta carpeta
        self.args[1].append("")
        self.args[1].append(self.ui.coloniaComboBox.getIdFromCurrentItem()[0])
        
    def cancelar(self):  
        self.close()

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = AgregarCurso()
    myapp.show()
    sys.exit(app.exec_())