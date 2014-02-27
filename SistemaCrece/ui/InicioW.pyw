#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys

from PyQt4.QtCore import pyqtSignal
from Inicio import Ui_Form
import PrincipalW

class Inicio(QtGui.QMainWindow):

    closed = pyqtSignal()
    peticion = pyqtSignal()
    obtenerInfo = pyqtSignal()
    exitApp = pyqtSignal()

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Sistema Crece")
        self.args = ["", [], ""]
        self.aceptar = False
        self.usuario = ""
        self.permisos = -1

    def ingresar(self):
        self.args = ["", [], ""]
        usuario = str(self.ui.usuarioTxt.text())
        contrasena = str(self.ui.contrasenaTxt.text())
        if self.verificarLocal(usuario, contrasena):
            self.obtenerInfo.emit()
            self.close()
        else:
            '''
            args -> tupla 3 elementos
            args[0] = nombre procedimiento
            args[1] = argumentos
            args[2] = tipo de retorno (tabla, string, comboBox)
            ''' 
            self.args[0] = "verificarUsuarioContrasena"
            self.args[1].append(usuario)
            self.args[1].append(contrasena)
            self.args[2] = "tabla"
            self.dataTypeFlag = 1
            self.peticion.emit()
        
    def verificarLocal(self, usuario, contrasena):
        #usuario y contrasena de capturista   
        if usuario == "capturistaCrece" and contrasena == "Cap2780C":
            self.usuario = "capturista"
            self.permisos = 5
            return True
        return False 
    
    def verificarBD(self, res):
        if res != None and len(res) != 0 :
            try:
                self.usuario = res[1][0]
                self.permisos= res[1][1] 
                self.obtenerInfo.emit()
                self.aceptar = True
                self.close()
            except Exception, e:
                self.mostrarMensaje("Usuario o contraseña invalida !!", 1)
                self.ui.contrasenaTxt.setText("")
                self.ui.usuarioTxt.setText("")       
                print e     
        else:
            self.mostrarMensaje("Usuario o contraseña invalida !!", 1)
            self.ui.contrasenaTxt.setText("")
            self.ui.usuarioTxt.setText("") 
    
    def mostrarMensaje(self, mensaje, tipoMensaje):   
        if tipoMensaje == 1:
            QtGui.QMessageBox.critical(self, 'Error !', mensaje, QtGui.QMessageBox.Ok)
        elif tipoMensaje == 0 and self.estaActualizando == False:
            print "mostrar mensaje inicio"
            QtGui.QMessageBox.information(self, "Mensaje", mensaje, QtGui.QMessageBox.Ok) 
        
    def recuperarContrasena(self):
        self.args = ["", [], ""]
        value = ""
        (value, ok) = QtGui.QInputDialog.getText(self, "Ingresa tu usuario", "Usuario: ", 
                                                QtGui.QLineEdit.Normal, value)
        if ok is False:
            return
        else:
            value2 = ""
            (value2, ok) = QtGui.QInputDialog.getText(self, "Ingresa tu email", "E-Mail: ", 
                                                QtGui.QLineEdit.Normal, value2)
            if ok is False:
                return
            else:
                self.args[0] = "recuperarContrasena"
                self.args[1].append(str(value))
                self.args[1].append(str(value2))
                self.args[2] = "recoveryType"
                print "recuperando contra ", self.args[0], " - ", self.args[1], " - ", self.args[2]
                self.dataTypeFlag = 0
                self.peticion.emit()
                return
            
    def closeEvent(self, event):
        if not self.aceptar:
            self.exitApp.emit()
            print "si exit!!!"
        else:
            self.closed.emit()
        event.accept()
        

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Inicio()
    myapp.show()
    sys.exit(app.exec_())