# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Inicio.ui'
#
# Created: Mon Jun 17 23:17:29 2013
#      by: PyQt4 UI code generator 4.10
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
        Form.resize(214, 127)
        self.usuarioLbl = QtGui.QLabel(Form)
        self.usuarioLbl.setGeometry(QtCore.QRect(20, 30, 46, 13))
        self.usuarioLbl.setObjectName(_fromUtf8("usuarioLbl"))
        self.contrasenaLbl_2 = QtGui.QLabel(Form)
        self.contrasenaLbl_2.setGeometry(QtCore.QRect(20, 60, 61, 16))
        self.contrasenaLbl_2.setObjectName(_fromUtf8("contrasenaLbl_2"))
        self.ingresarBtn = QtGui.QPushButton(Form)
        self.ingresarBtn.setGeometry(QtCore.QRect(130, 90, 75, 23))
        self.ingresarBtn.setObjectName(_fromUtf8("ingresarBtn"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(90, 30, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 60, 113, 20))
        self.lineEdit_2.setInputMask(_fromUtf8(""))
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.PasswordEchoOnEdit)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.ingresarBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.ingresar)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.usuarioLbl.setText(_translate("Form", "Usuario:", None))
        self.contrasenaLbl_2.setText(_translate("Form", "Contraseña:", None))
        self.ingresarBtn.setText(_translate("Form", "Ingresar", None))

