# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AgregarViaDonacion.ui'
#
# Created: Sun Jun 16 14:13:02 2013
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
        Form.resize(239, 83)
        self.viaDonacionTxt = QtGui.QLineEdit(Form)
        self.viaDonacionTxt.setGeometry(QtCore.QRect(100, 20, 113, 20))
        self.viaDonacionTxt.setObjectName(_fromUtf8("viaDonacionTxt"))
        self.viaDonacionLbl = QtGui.QLabel(Form)
        self.viaDonacionLbl.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.viaDonacionLbl.setObjectName(_fromUtf8("viaDonacionLbl"))
        self.aceptarBtn = QtGui.QPushButton(Form)
        self.aceptarBtn.setGeometry(QtCore.QRect(30, 50, 75, 23))
        self.aceptarBtn.setObjectName(_fromUtf8("aceptarBtn"))
        self.cancelarBtn = QtGui.QPushButton(Form)
        self.cancelarBtn.setGeometry(QtCore.QRect(140, 50, 75, 23))
        self.cancelarBtn.setObjectName(_fromUtf8("cancelarBtn"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.aceptarBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.agregarViaDonacion)
        QtCore.QObject.connect(self.cancelarBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.cancelar)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.viaDonacionLbl.setText(_translate("Form", "Via Donacion:", None))
        self.aceptarBtn.setText(_translate("Form", "Aceptar", None))
        self.cancelarBtn.setText(_translate("Form", "Cancelar", None))

