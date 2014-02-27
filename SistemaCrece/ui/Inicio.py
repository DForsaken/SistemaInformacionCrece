# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Inicio.ui'
#
# Created: Wed Feb 26 00:26:39 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(256, 128)
        self.usuarioLbl = QtGui.QLabel(Form)
        self.usuarioLbl.setGeometry(QtCore.QRect(20, 30, 46, 13))
        self.usuarioLbl.setObjectName(_fromUtf8("usuarioLbl"))
        self.contrasenaLbl_2 = QtGui.QLabel(Form)
        self.contrasenaLbl_2.setGeometry(QtCore.QRect(20, 60, 61, 16))
        self.contrasenaLbl_2.setObjectName(_fromUtf8("contrasenaLbl_2"))
        self.ingresarBtn = QtGui.QPushButton(Form)
        self.ingresarBtn.setGeometry(QtCore.QRect(160, 90, 75, 23))
        self.ingresarBtn.setObjectName(_fromUtf8("ingresarBtn"))
        self.usuarioTxt = QtGui.QLineEdit(Form)
        self.usuarioTxt.setGeometry(QtCore.QRect(90, 30, 141, 20))
        self.usuarioTxt.setObjectName(_fromUtf8("usuarioTxt"))
        self.contrasenaTxt = QtGui.QLineEdit(Form)
        self.contrasenaTxt.setGeometry(QtCore.QRect(90, 60, 141, 20))
        self.contrasenaTxt.setInputMask(_fromUtf8(""))
        self.contrasenaTxt.setEchoMode(QtGui.QLineEdit.Password)
        self.contrasenaTxt.setObjectName(_fromUtf8("contrasenaTxt"))
        self.recuperarContrasenaBtn = QtGui.QPushButton(Form)
        self.recuperarContrasenaBtn.setGeometry(QtCore.QRect(0, 100, 121, 23))
        self.recuperarContrasenaBtn.setFlat(True)
        self.recuperarContrasenaBtn.setObjectName(_fromUtf8("recuperarContrasenaBtn"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.ingresarBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.ingresar)
        QtCore.QObject.connect(self.recuperarContrasenaBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.recuperarContrasena)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Sistema Crece", None))
        self.usuarioLbl.setText(_translate("Form", "Usuario:", None))
        self.contrasenaLbl_2.setText(_translate("Form", "Contraseña:", None))
        self.ingresarBtn.setText(_translate("Form", "Ingresar", None))
        self.recuperarContrasenaBtn.setText(_translate("Form", "Recuperar contraseña", None))

