# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AgregarClasificacion.ui'
#
# Created: Sun Jun 16 14:11:13 2013
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
        Form.resize(224, 89)
        self.clasificacionLbl = QtGui.QLabel(Form)
        self.clasificacionLbl.setGeometry(QtCore.QRect(20, 10, 71, 16))
        self.clasificacionLbl.setObjectName(_fromUtf8("clasificacionLbl"))
        self.clasificacionTxt = QtGui.QLineEdit(Form)
        self.clasificacionTxt.setGeometry(QtCore.QRect(90, 10, 113, 20))
        self.clasificacionTxt.setObjectName(_fromUtf8("clasificacionTxt"))
        self.aceptarBtn = QtGui.QPushButton(Form)
        self.aceptarBtn.setGeometry(QtCore.QRect(30, 50, 75, 23))
        self.aceptarBtn.setObjectName(_fromUtf8("aceptarBtn"))
        self.cancelarBtn = QtGui.QPushButton(Form)
        self.cancelarBtn.setGeometry(QtCore.QRect(130, 50, 75, 23))
        self.cancelarBtn.setObjectName(_fromUtf8("cancelarBtn"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.aceptarBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.agregarClasificacion)
        QtCore.QObject.connect(self.cancelarBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.cancelar)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.clasificacionLbl.setText(_translate("Form", "Clasificación:", None))
        self.aceptarBtn.setText(_translate("Form", "Aceptar", None))
        self.cancelarBtn.setText(_translate("Form", "Cancelar", None))

