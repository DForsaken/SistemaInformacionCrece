# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AgregarCausaFalta.ui'
#
# Created: Sun Jun 16 14:10:54 2013
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
        Form.resize(212, 116)
        self.causaLbl = QtGui.QLabel(Form)
        self.causaLbl.setGeometry(QtCore.QRect(20, 20, 46, 13))
        self.causaLbl.setObjectName(_fromUtf8("causaLbl"))
        self.descripcionLbl = QtGui.QLabel(Form)
        self.descripcionLbl.setGeometry(QtCore.QRect(20, 50, 61, 16))
        self.descripcionLbl.setObjectName(_fromUtf8("descripcionLbl"))
        self.causaTxt = QtGui.QLineEdit(Form)
        self.causaTxt.setGeometry(QtCore.QRect(90, 20, 113, 20))
        self.causaTxt.setObjectName(_fromUtf8("causaTxt"))
        self.descripcionTxt = QtGui.QLineEdit(Form)
        self.descripcionTxt.setGeometry(QtCore.QRect(90, 50, 113, 20))
        self.descripcionTxt.setObjectName(_fromUtf8("descripcionTxt"))
        self.aceptarBtn = QtGui.QPushButton(Form)
        self.aceptarBtn.setGeometry(QtCore.QRect(30, 80, 75, 23))
        self.aceptarBtn.setObjectName(_fromUtf8("aceptarBtn"))
        self.cancelarBtn = QtGui.QPushButton(Form)
        self.cancelarBtn.setGeometry(QtCore.QRect(130, 80, 75, 23))
        self.cancelarBtn.setObjectName(_fromUtf8("cancelarBtn"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.aceptarBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.agregarCausaFalta)
        QtCore.QObject.connect(self.cancelarBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.cancelar)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.causaLbl.setText(_translate("Form", "Causa:", None))
        self.descripcionLbl.setText(_translate("Form", "Descripción:", None))
        self.aceptarBtn.setText(_translate("Form", "Aceptar", None))
        self.cancelarBtn.setText(_translate("Form", "Cancelar", None))

