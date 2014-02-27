# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AgregarEscuela.ui'
#
# Created: Sun Jun 16 14:12:06 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import QComboBoxWrapper

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
        Form.resize(233, 216)
        self.nombreLbl = QtGui.QLabel(Form)
        self.nombreLbl.setGeometry(QtCore.QRect(20, 20, 46, 13))
        self.nombreLbl.setObjectName(_fromUtf8("nombreLbl"))
        self.domicilioLbl = QtGui.QLabel(Form)
        self.domicilioLbl.setGeometry(QtCore.QRect(20, 50, 46, 13))
        self.domicilioLbl.setObjectName(_fromUtf8("domicilioLbl"))
        self.codigoPostalLbl = QtGui.QLabel(Form)
        self.codigoPostalLbl.setGeometry(QtCore.QRect(20, 80, 71, 16))
        self.codigoPostalLbl.setObjectName(_fromUtf8("codigoPostalLbl"))
        self.telefonoLbl = QtGui.QLabel(Form)
        self.telefonoLbl.setGeometry(QtCore.QRect(20, 110, 46, 13))
        self.telefonoLbl.setObjectName(_fromUtf8("telefonoLbl"))
        self.coloniaLbl = QtGui.QLabel(Form)
        self.coloniaLbl.setGeometry(QtCore.QRect(20, 140, 46, 13))
        self.coloniaLbl.setObjectName(_fromUtf8("coloniaLbl"))
        self.codigoPostalTxt = QtGui.QLineEdit(Form)
        self.codigoPostalTxt.setGeometry(QtCore.QRect(100, 80, 113, 20))
        self.codigoPostalTxt.setObjectName(_fromUtf8("codigoPostalTxt"))
        self.nombreTxt = QtGui.QLineEdit(Form)
        self.nombreTxt.setGeometry(QtCore.QRect(100, 20, 113, 20))
        self.nombreTxt.setObjectName(_fromUtf8("nombreTxt"))
        self.domicilioTxt = QtGui.QLineEdit(Form)
        self.domicilioTxt.setGeometry(QtCore.QRect(100, 50, 113, 20))
        self.domicilioTxt.setObjectName(_fromUtf8("domicilioTxt"))
        self.telefonoTxt = QtGui.QLineEdit(Form)
        self.telefonoTxt.setGeometry(QtCore.QRect(100, 110, 113, 20))
        self.telefonoTxt.setObjectName(_fromUtf8("telefonoTxt"))
        self.ColoniaComboBox = QComboBoxWrapper.QComboBoxWrapper(Form)
        self.ColoniaComboBox.setGeometry(QtCore.QRect(100, 140, 111, 21))
        self.ColoniaComboBox.setObjectName(_fromUtf8("ColoniaComboBox"))
        self.aceptarBtn = QtGui.QPushButton(Form)
        self.aceptarBtn.setGeometry(QtCore.QRect(30, 180, 75, 23))
        self.aceptarBtn.setObjectName(_fromUtf8("aceptarBtn"))
        self.cancelarBtnb = QtGui.QPushButton(Form)
        self.cancelarBtnb.setGeometry(QtCore.QRect(140, 180, 75, 23))
        self.cancelarBtnb.setObjectName(_fromUtf8("cancelarBtnb"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.aceptarBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.agregarEscuela)
        QtCore.QObject.connect(self.cancelarBtnb, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.cancelar)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.nombreLbl.setText(_translate("Form", "Nombre:", None))
        self.domicilioLbl.setText(_translate("Form", "Domicilio:", None))
        self.codigoPostalLbl.setText(_translate("Form", "Codigo Postal:", None))
        self.telefonoLbl.setText(_translate("Form", "Telefono:", None))
        self.coloniaLbl.setText(_translate("Form", "Colonia:", None))
        self.aceptarBtn.setText(_translate("Form", "Aceptar", None))
        self.cancelarBtnb.setText(_translate("Form", "Cancelar", None))

