# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AgregarPersonaCurso.ui'
#
# Created: Sun Jun 16 14:12:35 2013
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
        Form.resize(224, 215)
        self.areaLbl = QtGui.QLabel(Form)
        self.areaLbl.setGeometry(QtCore.QRect(20, 20, 46, 13))
        self.areaLbl.setObjectName(_fromUtf8("areaLbl"))
        self.nombreLbl = QtGui.QLabel(Form)
        self.nombreLbl.setGeometry(QtCore.QRect(20, 50, 46, 13))
        self.nombreLbl.setObjectName(_fromUtf8("nombreLbl"))
        self.coloniaLbl = QtGui.QLabel(Form)
        self.coloniaLbl.setGeometry(QtCore.QRect(20, 80, 46, 13))
        self.coloniaLbl.setObjectName(_fromUtf8("coloniaLbl"))
        self.fechaInicioLbl = QtGui.QLabel(Form)
        self.fechaInicioLbl.setGeometry(QtCore.QRect(20, 110, 61, 16))
        self.fechaInicioLbl.setObjectName(_fromUtf8("fechaInicioLbl"))
        self.alumnoLbl = QtGui.QLabel(Form)
        self.alumnoLbl.setGeometry(QtCore.QRect(20, 140, 46, 13))
        self.alumnoLbl.setObjectName(_fromUtf8("alumnoLbl"))
        self.coloniaComboBox = QtGui.QComboBox(Form)
        self.coloniaComboBox.setGeometry(QtCore.QRect(90, 80, 111, 21))
        self.coloniaComboBox.setObjectName(_fromUtf8("coloniaComboBox"))
        self.nombreComboBox = QtGui.QComboBox(Form)
        self.nombreComboBox.setGeometry(QtCore.QRect(90, 50, 111, 21))
        self.nombreComboBox.setObjectName(_fromUtf8("nombreComboBox"))
        self.arecomboBox = QtGui.QComboBox(Form)
        self.arecomboBox.setGeometry(QtCore.QRect(90, 20, 111, 21))
        self.arecomboBox.setObjectName(_fromUtf8("arecomboBox"))
        self.alumnoComboBox = QtGui.QComboBox(Form)
        self.alumnoComboBox.setGeometry(QtCore.QRect(90, 140, 111, 21))
        self.alumnoComboBox.setObjectName(_fromUtf8("alumnoComboBox"))
        self.fechaInicioDate = QtGui.QDateEdit(Form)
        self.fechaInicioDate.setGeometry(QtCore.QRect(90, 110, 110, 21))
        self.fechaInicioDate.setObjectName(_fromUtf8("fechaInicioDate"))
        self.aceptarBtn = QtGui.QPushButton(Form)
        self.aceptarBtn.setGeometry(QtCore.QRect(20, 180, 75, 23))
        self.aceptarBtn.setObjectName(_fromUtf8("aceptarBtn"))
        self.CancelarBtn = QtGui.QPushButton(Form)
        self.CancelarBtn.setGeometry(QtCore.QRect(130, 180, 75, 23))
        self.CancelarBtn.setObjectName(_fromUtf8("CancelarBtn"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.aceptarBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.agregarPersonaCurso)
        QtCore.QObject.connect(self.CancelarBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.cancelar)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.areaLbl.setText(_translate("Form", "Área:", None))
        self.nombreLbl.setText(_translate("Form", "Nombre:", None))
        self.coloniaLbl.setText(_translate("Form", "Colonia:", None))
        self.fechaInicioLbl.setText(_translate("Form", "Fecha Inicio:", None))
        self.alumnoLbl.setText(_translate("Form", "Persona:", None))
        self.aceptarBtn.setText(_translate("Form", " Aceptar", None))
        self.CancelarBtn.setText(_translate("Form", "Cancelar", None))

