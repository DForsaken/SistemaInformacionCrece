#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys, comboBoxUtilities
from PyQt4.QtCore import pyqtSignal
from AgregarPersona import Ui_Form

class AgregarPersona(QtGui.QMainWindow):

    closed = pyqtSignal()
    agregar = pyqtSignal()
    peticion = pyqtSignal()

    def __init__(self, tipoPersona, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Sistema Crece")
        self.tipoPersona = tipoPersona
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
        self.establecerNombresEtiquetas()
        
    def establecerNombresEtiquetas(self):
        print  "TIPO /// ", self.tipoPersona
        if self.tipoPersona == "Practicante" or self.tipoPersona == "Prestador":
            self.ui.monitoreoAreaLbl.setText("Area:")
            self.ui.escuelaPuestoLbl.setText("Escuela:")
            self.ui.usuarioTelEmeLbl.setText("Tel Emergencia:")
            self.ui.contrasenaNombreResLbl.setText("Responsable:")
            self.ui.verifiContrasenaTelRespLbl.setText("Tel Responsable:")
            self.ui.permisosLbl.hide()
            self.ui.permisosComboBox.hide()
        elif self.tipoPersona == "Alumno" or self.tipoPersona == "Voluntario":
            self.ui.fechaFinLbl.hide()
            self.ui.fechaInicioLbl.hide()
            self.ui.fechaFinDate.hide()
            self.ui.fechaInicioDate.hide()
            self.ui.escuelaPuestoLbl.hide()
            self.ui.escuelaPuestoComboBox.hide()
            self.ui.usuarioTelEmeLbl.hide()
            self.ui.usuarioTelEmeTxt.hide()
            self.ui.contrasenaNombreResLbl.hide()
            self.ui.contrasenaNombreResTxt.hide()
            self.ui.verifiContrasenaTelRespLbl.hide()
            self.ui.verifiContrasenaTelRespTxt.hide()
            self.ui.emailRespLbl.hide()
            self.ui.emailRespTxt.hide()
            self.ui.permisosLbl.hide()
            self.ui.permisosComboBox.hide()
            if self.tipoPersona == "Voluntario":
                self.ui.monitoreoAreaLbl.hide()
                self.ui.monitoreoAreaComboBox.hide()
        elif self.tipoPersona == "Empleado":
            self.ui.fechaFinLbl.hide()
            self.ui.fechaInicioLbl.hide()
            self.ui.fechaFinDate.hide()
            self.ui.fechaInicioDate.hide()
            self.ui.monitoreoAreaLbl.setText("Area:")
            self.ui.escuelaPuestoLbl.setText("Puesto:")
            self.ui.usuarioTelEmeLbl.setText("Usuario:")
            self.ui.contrasenaNombreResTxt.setEchoMode(QtGui.QLineEdit.Password);
            self.ui.contrasenaNombreResLbl.setText("Contrasena:")
            self.ui.verifiContrasenaTelRespTxt.setEchoMode(QtGui.QLineEdit.Password);
            self.ui.verifiContrasenaTelRespLbl.setText("Verifica Contrasena:")
            self.ui.emailRespLbl.hide()
            self.ui.emailRespTxt.hide()
            
    def llenarComboBox(self):
        self.ui.generoComboBox.addItems("H")
        self.ui.generoComboBox.addItems("M")
        self.args[2] = "comboBox"
        self.comboBoxActual = self.ui.coloniaComboBox
        self.comboUtilities.setIndex("Colonia")
        self.ejectuarPeticion("verColonia")
        self.comboBoxActual = self.ui.gradoEscolarComboBox
        self.comboUtilities.setIndex("GradoEscolar")
        self.ejectuarPeticion("verGradoEscolar")
        if self.tipoPersona == "Practicante" or self.tipoPersona == "Prestador":
            self.comboBoxActual= self.ui.escuelaPuestoComboBox
            self.comboUtilities.setIndex("Escuela")
            self.ejectuarPeticion("verEscuela")
            self.comboBoxActual = self.ui.monitoreoAreaComboBox
            self.comboUtilities.setIndex("Area")
            self.ejectuarPeticion("verArea")
        elif self.tipoPersona == "Empleado":
            self.comboBoxActual = self.ui.monitoreoAreaComboBox
            self.comboUtilities.setIndex("Area")
            self.ejectuarPeticion("verArea")
            self.comboBoxActual= self.ui.escuelaPuestoComboBox
            self.comboUtilities.setIndex("Puesto")
            self.ejectuarPeticion("verPuesto")
            self.comboBoxActual = self.ui.permisosComboBox
            self.comboUtilities.setIndex("Permiso")
            self.ejectuarPeticion("verPermiso")
        elif self.tipoPersona == "Alumno":
            self.ui.monitoreoAreaComboBox.addItems("1")
            self.ui.monitoreoAreaComboBox.addItems("0")
        self.comboBoxActual = None

    def ejectuarPeticion(self, proc):
        self.args[0] = proc
        self.args[1] = []
        self.peticion.emit()
        print self.args[0]
            
    def obtenerComboBox(self, res):
        self.comboUtilities.populateComboBox(self.comboBoxActual, res)
                    
    def definirArgs(self):
        self.args[0] = "insertar" + self.tipoPersona

    def agregarPersona(self):
        self.args = ["",[],""]
        if self.tipoPersona == "Empleado":
            if not(str(self.ui.contrasenaNombreResTxt.text()) == 
                        str(self.ui.verifiContrasenaTelRespTxt.text())):
                self.mostrarMensaje("Las constrasenas no coinciden")
                return
        try:
            self.prepararPersonaArgs()
            self.preparTipoPersonaArgs()
        except ValueError:
            self.mostrarMensaje("Inserta solo valores numericos en los campos numericos !")
            return
        for i in range(0,len(self.args[1])):
            print " - ", self.args[1][i]
        if self.tipoPersona == "Empleado":
            self.args[0] = "inserta" + self.tipoPersona
        elif self.tipoPersona == "Practicante" or self.tipoPersona == "Prestador":
            self.args[0] = "insertaEstudiante"
        else:
            self.args[0] = "insertaPersona"
        self.args[2] = "string"
        self.dataTypeFlag = 0 
        self.agregar.emit()
        self.cancelar()

    def preparTipoPersonaArgs(self):
        if self.tipoPersona == "Empleado":
            self.args[1].append(str(self.ui.usuarioTelEmeTxt.text()))
            self.args[1].append(str(self.ui.contrasenaNombreResTxt.text()))
            self.args[1].append(self.ui.monitoreoAreaComboBox.getIdFromCurrentItem()[0])
            self.args[1].append(self.ui.escuelaPuestoComboBox.getIdFromCurrentItem()[0])
        elif self.tipoPersona == "Practicante" or self.tipoPersona == "Prestador":
            for i in self.ui.escuelaPuestoComboBox.getIdFromCurrentItem():
                self.args[1].append(i)
            self.args[1].append(str(self.ui.usuarioTelEmeTxt.text()))
            self.args[1].append(str((self.ui.fechaInicioDate.text()).replace("/","-")))
            self.args[1].append(str((self.ui.fechaFinDate.text()).replace("/","-")))
            self.args[1].append(str(self.ui.contrasenaNombreResTxt.text()))
            self.args[1].append(str(self.ui.verifiContrasenaTelRespTxt.text()))
            self.args[1].append(str(self.ui.emailRespTxt.text()))
            
    def prepararPersonaArgs(self):
        self.args[1].append(str(self.ui.nombreTxt.text()))
        self.args[1].append(str(self.ui.apTxt.text()))
        self.args[1].append(str(self.ui.amTxt.text()))
        self.args[1].append(str(self.ui.generoComboBox.itemText(self.ui.generoComboBox.currentIndex())))
        self.args[1].append(str((self.ui.fechaNacDate.text()).replace("/","-")))
        self.args[1].append(str(self.ui.domicilioTxt.text()))
        self.args[1].append(self.ui.coloniaComboBox.getIdFromCurrentItem()[0])
        self.args[1].append(int(self.ui.codigoPostalTxt.text()))
        for i in self.ui.gradoEscolarComboBox.getIdFromCurrentItem():
            self.args[1].append(i)      
        self.args[1].append(str(self.ui.telefonoTxt.text()))
        self.args[1].append(str(self.ui.celularTxt.text()))
        self.args[1].append(str(self.ui.emailTxt.text()))
        #estatus persona
        self.args[1].append(1)
        #ruta carpeta
        self.args[1].append("")
        #monitero
        if self.tipoPersona == "Alumno":
            self.args[1].append(int(self.ui.monitoreoAreaComboBox.itemText(
                                                self.ui.monitoreoAreaComboBox.currentIndex())))
        elif self.tipoPersona == "Practicante" or self.tipoPersona == "Prestador":
            self.args[1].append(str(self.ui.monitoreoAreaComboBox.itemText(
                                                self.ui.monitoreoAreaComboBox.currentIndex())))
        else:
            self.args[1].append(0)
        self.args[1].append(self.tipoPersona)
        #permisos
        if self.tipoPersona == "Practicante" or self.tipoPersona == "Prestador" or self.tipoPersona == "Voluntario":
            self.args[1].append("capturista")
        elif self.tipoPersona == "Empleado":
            self.args[1].append(self.ui.permisosComboBox.getIdFromCurrentItem()[0])
        elif self.tipoPersona == "Alumno":
            self.args[1].append("ninguno")
            
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
    myapp = AgregarPersona()
    myapp.show()
    sys.exit(app.exec_())