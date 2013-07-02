# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EscojerCurso.ui'
#
# Created: Sun Jun 16 14:13:33 2013
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
        Form.resize(228, 173)
        self.fechaInicioDate = QtGui.QDateEdit(Form)
        self.fechaInicioDate.setGeometry(QtCore.QRect(90, 100, 110, 21))
        self.fechaInicioDate.setObjectName(_fromUtf8("fechaInicioDate"))
        self.nombreLbl = QtGui.QLabel(Form)
        self.nombreLbl.setGeometry(QtCore.QRect(20, 40, 46, 13))
        self.nombreLbl.setObjectName(_fromUtf8("nombreLbl"))
        self.aceptarBtn = QtGui.QPushButton(Form)
        self.aceptarBtn.setGeometry(QtCore.QRect(130, 130, 75, 23))
        self.aceptarBtn.setObjectName(_fromUtf8("aceptarBtn"))
        self.areaLbl = QtGui.QLabel(Form)
        self.areaLbl.setGeometry(QtCore.QRect(20, 10, 46, 13))
        self.areaLbl.setObjectName(_fromUtf8("areaLbl"))
        self.nombreComboBox = QtGui.QComboBox(Form)
        self.nombreComboBox.setGeometry(QtCore.QRect(90, 40, 111, 21))
        self.nombreComboBox.setObjectName(_fromUtf8("nombreComboBox"))
        self.coloniaLbl = QtGui.QLabel(Form)
        self.coloniaLbl.setGeometry(QtCore.QRect(20, 70, 46, 13))
        self.coloniaLbl.setObjectName(_fromUtf8("coloniaLbl"))
        self.fechaInicioLbl = QtGui.QLabel(Form)
        self.fechaInicioLbl.setGeometry(QtCore.QRect(20, 100, 61, 16))
        self.fechaInicioLbl.setObjectName(_fromUtf8("fechaInicioLbl"))
        self.arecomboBox = QtGui.QComboBox(Form)
        self.arecomboBox.setGeometry(QtCore.QRect(90, 10, 111, 21))
        self.arecomboBox.setObjectName(_fromUtf8("arecomboBox"))
        self.coloniaComboBox = QtGui.QComboBox(Form)
        self.coloniaComboBox.setGeometry(QtCore.QRect(90, 70, 111, 21))
        self.coloniaComboBox.setObjectName(_fromUtf8("coloniaComboBox"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.aceptarBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.escojerCurso)
        QtCore.QObject.connect(self.aceptarBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.cancelar)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.nombreLbl.setText(_translate("Form", "Nombre:", None))
        self.aceptarBtn.setText(_translate("Form", " Aceptar", None))
        self.areaLbl.setText(_translate("Form", "Área:", None))
        self.coloniaLbl.setText(_translate("Form", "Colonia:", None))
        self.fechaInicioLbl.setText(_translate("Form", "Fecha Inicio:", None))

