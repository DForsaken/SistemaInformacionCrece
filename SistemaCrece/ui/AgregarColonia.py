# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AgregarColonia.ui'
#
# Created: Sun Jun 16 14:11:31 2013
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
        Form.resize(211, 124)
        self.nombreLbl = QtGui.QLabel(Form)
        self.nombreLbl.setGeometry(QtCore.QRect(20, 20, 46, 13))
        self.nombreLbl.setObjectName(_fromUtf8("nombreLbl"))
        self.municipioLbl = QtGui.QLabel(Form)
        self.municipioLbl.setGeometry(QtCore.QRect(20, 50, 51, 16))
        self.municipioLbl.setObjectName(_fromUtf8("municipioLbl"))
        self.nombreTxt = QtGui.QLineEdit(Form)
        self.nombreTxt.setGeometry(QtCore.QRect(70, 20, 113, 20))
        self.nombreTxt.setObjectName(_fromUtf8("nombreTxt"))
        self.municipioTxt = QtGui.QLineEdit(Form)
        self.municipioTxt.setGeometry(QtCore.QRect(70, 50, 113, 20))
        self.municipioTxt.setObjectName(_fromUtf8("municipioTxt"))
        self.aceptarBtn = QtGui.QPushButton(Form)
        self.aceptarBtn.setGeometry(QtCore.QRect(10, 80, 75, 23))
        self.aceptarBtn.setObjectName(_fromUtf8("aceptarBtn"))
        self.cancelarBtn = QtGui.QPushButton(Form)
        self.cancelarBtn.setGeometry(QtCore.QRect(110, 80, 75, 23))
        self.cancelarBtn.setObjectName(_fromUtf8("cancelarBtn"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.aceptarBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.agregarColonia)
        QtCore.QObject.connect(self.cancelarBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.cancelar)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.nombreLbl.setText(_translate("Form", "Nombre:", None))
        self.municipioLbl.setText(_translate("Form", "Municipio:", None))
        self.aceptarBtn.setText(_translate("Form", "Aceptar", None))
        self.cancelarBtn.setText(_translate("Form", "Cancelar", None))

