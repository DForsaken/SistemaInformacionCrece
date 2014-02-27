# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AgregarDonador.ui'
#
# Created: Sat Feb 08 21:39:00 2014
#      by: PyQt4 UI code generator 4.10.3
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
        Form.resize(221, 329)
        self.nombreLbl = QtGui.QLabel(Form)
        self.nombreLbl.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.nombreLbl.setObjectName(_fromUtf8("nombreLbl"))
        self.direccionLbl = QtGui.QLabel(Form)
        self.direccionLbl.setGeometry(QtCore.QRect(20, 50, 46, 13))
        self.direccionLbl.setObjectName(_fromUtf8("direccionLbl"))
        self.telefonoLbl = QtGui.QLabel(Form)
        self.telefonoLbl.setGeometry(QtCore.QRect(20, 80, 51, 16))
        self.telefonoLbl.setObjectName(_fromUtf8("telefonoLbl"))
        self.emailLbl = QtGui.QLabel(Form)
        self.emailLbl.setGeometry(QtCore.QRect(20, 110, 46, 13))
        self.emailLbl.setObjectName(_fromUtf8("emailLbl"))
        self.clasificacionLbl = QtGui.QLabel(Form)
        self.clasificacionLbl.setGeometry(QtCore.QRect(20, 140, 61, 16))
        self.clasificacionLbl.setObjectName(_fromUtf8("clasificacionLbl"))
        self.viaDonacionLbl = QtGui.QLabel(Form)
        self.viaDonacionLbl.setGeometry(QtCore.QRect(20, 170, 71, 16))
        self.viaDonacionLbl.setObjectName(_fromUtf8("viaDonacionLbl"))
        self.cantidadLbl = QtGui.QLabel(Form)
        self.cantidadLbl.setGeometry(QtCore.QRect(20, 200, 51, 16))
        self.cantidadLbl.setObjectName(_fromUtf8("cantidadLbl"))
        self.fechaSalidaLbl = QtGui.QLabel(Form)
        self.fechaSalidaLbl.setGeometry(QtCore.QRect(20, 230, 71, 16))
        self.fechaSalidaLbl.setObjectName(_fromUtf8("fechaSalidaLbl"))
        self.fechaInicioLbl = QtGui.QLabel(Form)
        self.fechaInicioLbl.setGeometry(QtCore.QRect(20, 260, 61, 16))
        self.fechaInicioLbl.setObjectName(_fromUtf8("fechaInicioLbl"))
        self.cantidadTxt = QtGui.QLineEdit(Form)
        self.cantidadTxt.setGeometry(QtCore.QRect(90, 200, 113, 20))
        self.cantidadTxt.setObjectName(_fromUtf8("cantidadTxt"))
        self.nombreTxt = QtGui.QLineEdit(Form)
        self.nombreTxt.setGeometry(QtCore.QRect(90, 20, 113, 20))
        self.nombreTxt.setObjectName(_fromUtf8("nombreTxt"))
        self.direccionTxt = QtGui.QLineEdit(Form)
        self.direccionTxt.setGeometry(QtCore.QRect(90, 50, 113, 20))
        self.direccionTxt.setObjectName(_fromUtf8("direccionTxt"))
        self.telefonoTxt = QtGui.QLineEdit(Form)
        self.telefonoTxt.setGeometry(QtCore.QRect(90, 80, 113, 20))
        self.telefonoTxt.setObjectName(_fromUtf8("telefonoTxt"))
        self.emailTxt = QtGui.QLineEdit(Form)
        self.emailTxt.setGeometry(QtCore.QRect(90, 110, 113, 20))
        self.emailTxt.setObjectName(_fromUtf8("emailTxt"))
        self.clasificacionComboBox = QComboBoxWrapper.QComboBoxWrapper(Form)
        self.clasificacionComboBox.setGeometry(QtCore.QRect(90, 140, 111, 21))
        self.clasificacionComboBox.setObjectName(_fromUtf8("clasificacionComboBox"))
        self.viaDonacionComboBox = QComboBoxWrapper.QComboBoxWrapper(Form)
        self.viaDonacionComboBox.setGeometry(QtCore.QRect(90, 170, 111, 21))
        self.viaDonacionComboBox.setObjectName(_fromUtf8("viaDonacionComboBox"))
        self.fechaInicioDate = QtGui.QDateEdit(Form)
        self.fechaInicioDate.setGeometry(QtCore.QRect(90, 230, 110, 21))
        self.fechaInicioDate.setObjectName(_fromUtf8("fechaInicioDate"))
        self.fechaFinDate = QtGui.QDateEdit(Form)
        self.fechaFinDate.setGeometry(QtCore.QRect(90, 260, 110, 21))
        self.fechaFinDate.setObjectName(_fromUtf8("fechaFinDate"))
        self.AceptarBtn = QtGui.QPushButton(Form)
        self.AceptarBtn.setGeometry(QtCore.QRect(20, 290, 75, 23))
        self.AceptarBtn.setObjectName(_fromUtf8("AceptarBtn"))
        self.CancelarBtn = QtGui.QPushButton(Form)
        self.CancelarBtn.setGeometry(QtCore.QRect(130, 290, 75, 23))
        self.CancelarBtn.setObjectName(_fromUtf8("CancelarBtn"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.AceptarBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.agregarDonador)
        QtCore.QObject.connect(self.CancelarBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.cancelar)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.nombreLbl.setText(_translate("Form", "Nombre:", None))
        self.direccionLbl.setText(_translate("Form", "Dirección:", None))
        self.telefonoLbl.setText(_translate("Form", "Telefono:", None))
        self.emailLbl.setText(_translate("Form", "E-Mail:", None))
        self.clasificacionLbl.setText(_translate("Form", "Clasificación:", None))
        self.viaDonacionLbl.setText(_translate("Form", "Vía Donación:", None))
        self.cantidadLbl.setText(_translate("Form", "Cantidad:", None))
        self.fechaSalidaLbl.setText(_translate("Form", "Fecha Salida:", None))
        self.fechaInicioLbl.setText(_translate("Form", "Fecha Inicio:", None))
        self.fechaInicioDate.setDisplayFormat(_translate("Form", "yyyy/MM/dd", None))
        self.fechaFinDate.setDisplayFormat(_translate("Form", "yyyy/MM/dd", None))
        self.AceptarBtn.setText(_translate("Form", "Aceptar", None))
        self.CancelarBtn.setText(_translate("Form", "Cancelar", None))

