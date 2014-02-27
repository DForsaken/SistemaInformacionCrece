# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AgregarCurso.ui'
#
# Created: Thu Feb 06 22:33:37 2014
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
        Form.resize(228, 319)
        self.nombreLbl = QtGui.QLabel(Form)
        self.nombreLbl.setGeometry(QtCore.QRect(20, 20, 46, 13))
        self.nombreLbl.setObjectName(_fromUtf8("nombreLbl"))
        self.coloniaLbl = QtGui.QLabel(Form)
        self.coloniaLbl.setGeometry(QtCore.QRect(20, 50, 46, 13))
        self.coloniaLbl.setObjectName(_fromUtf8("coloniaLbl"))
        self.areaLbl = QtGui.QLabel(Form)
        self.areaLbl.setGeometry(QtCore.QRect(20, 80, 46, 13))
        self.areaLbl.setObjectName(_fromUtf8("areaLbl"))
        self.fechaInicioLbl = QtGui.QLabel(Form)
        self.fechaInicioLbl.setGeometry(QtCore.QRect(20, 110, 61, 16))
        self.fechaInicioLbl.setObjectName(_fromUtf8("fechaInicioLbl"))
        self.fechaFinLbl = QtGui.QLabel(Form)
        self.fechaFinLbl.setGeometry(QtCore.QRect(20, 140, 61, 16))
        self.fechaFinLbl.setObjectName(_fromUtf8("fechaFinLbl"))
        self.enfoqueLbl = QtGui.QLabel(Form)
        self.enfoqueLbl.setGeometry(QtCore.QRect(20, 170, 46, 13))
        self.enfoqueLbl.setObjectName(_fromUtf8("enfoqueLbl"))
        self.nombreTxt = QtGui.QLineEdit(Form)
        self.nombreTxt.setGeometry(QtCore.QRect(90, 20, 113, 20))
        self.nombreTxt.setObjectName(_fromUtf8("nombreTxt"))
        self.enfoqueTxt = QtGui.QTextEdit(Form)
        self.enfoqueTxt.setGeometry(QtCore.QRect(90, 170, 111, 91))
        self.enfoqueTxt.setObjectName(_fromUtf8("enfoqueTxt"))
        self.fechaInicioDate = QtGui.QDateEdit(Form)
        self.fechaInicioDate.setGeometry(QtCore.QRect(90, 140, 110, 21))
        self.fechaInicioDate.setObjectName(_fromUtf8("fechaInicioDate"))
        self.fechaFinDate = QtGui.QDateEdit(Form)
        self.fechaFinDate.setGeometry(QtCore.QRect(90, 110, 110, 21))
        self.fechaFinDate.setObjectName(_fromUtf8("fechaFinDate"))
        self.areaComboBox = QComboBoxWrapper.QComboBoxWrapper(Form)
        self.areaComboBox.setGeometry(QtCore.QRect(90, 80, 111, 22))
        self.areaComboBox.setObjectName(_fromUtf8("areaComboBox"))
        self.coloniaComboBox = QComboBoxWrapper.QComboBoxWrapper(Form)
        self.coloniaComboBox.setGeometry(QtCore.QRect(90, 50, 111, 22))
        self.coloniaComboBox.setObjectName(_fromUtf8("coloniaComboBox"))
        self.aceptarBtn = QtGui.QPushButton(Form)
        self.aceptarBtn.setGeometry(QtCore.QRect(20, 280, 75, 23))
        self.aceptarBtn.setObjectName(_fromUtf8("aceptarBtn"))
        self.cancelarBtn = QtGui.QPushButton(Form)
        self.cancelarBtn.setGeometry(QtCore.QRect(120, 280, 75, 23))
        self.cancelarBtn.setObjectName(_fromUtf8("cancelarBtn"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.aceptarBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.agregarCurso)
        QtCore.QObject.connect(self.cancelarBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.cancelar)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.nombreLbl.setText(_translate("Form", "Nombre:", None))
        self.coloniaLbl.setText(_translate("Form", "Colonia:", None))
        self.areaLbl.setText(_translate("Form", "Area:", None))
        self.fechaInicioLbl.setText(_translate("Form", "Fecha inicio:", None))
        self.fechaFinLbl.setText(_translate("Form", "Fecha fin:", None))
        self.enfoqueLbl.setText(_translate("Form", "Enfoque:", None))
        self.fechaInicioDate.setDisplayFormat(_translate("Form", "yyyy/MM/dd", None))
        self.fechaFinDate.setDisplayFormat(_translate("Form", "yyyy/MM/dd", None))
        self.aceptarBtn.setText(_translate("Form", "Aceptar", None))
        self.cancelarBtn.setText(_translate("Form", "Cancelar", None))

