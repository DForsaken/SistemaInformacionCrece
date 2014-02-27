# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EscogerDiasSemana.ui'
#
# Created: Sun Feb 16 22:39:25 2014
#      by: PyQt4 UI code generator 4.10.3
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
        Form.resize(177, 277)
        self.diasGroupBox = QtGui.QGroupBox(Form)
        self.diasGroupBox.setGeometry(QtCore.QRect(10, 20, 151, 211))
        self.diasGroupBox.setObjectName(_fromUtf8("diasGroupBox"))
        self.lunesCheckBox = QtGui.QCheckBox(self.diasGroupBox)
        self.lunesCheckBox.setGeometry(QtCore.QRect(30, 30, 70, 17))
        self.lunesCheckBox.setObjectName(_fromUtf8("lunesCheckBox"))
        self.martesCheckBox = QtGui.QCheckBox(self.diasGroupBox)
        self.martesCheckBox.setGeometry(QtCore.QRect(30, 60, 70, 17))
        self.martesCheckBox.setObjectName(_fromUtf8("martesCheckBox"))
        self.miercolesCheckBox = QtGui.QCheckBox(self.diasGroupBox)
        self.miercolesCheckBox.setGeometry(QtCore.QRect(30, 90, 70, 17))
        self.miercolesCheckBox.setObjectName(_fromUtf8("miercolesCheckBox"))
        self.juevesCheckBox = QtGui.QCheckBox(self.diasGroupBox)
        self.juevesCheckBox.setGeometry(QtCore.QRect(30, 120, 70, 17))
        self.juevesCheckBox.setObjectName(_fromUtf8("juevesCheckBox"))
        self.viernesCheckBox = QtGui.QCheckBox(self.diasGroupBox)
        self.viernesCheckBox.setGeometry(QtCore.QRect(30, 150, 70, 17))
        self.viernesCheckBox.setObjectName(_fromUtf8("viernesCheckBox"))
        self.sabadoCheckBox = QtGui.QCheckBox(self.diasGroupBox)
        self.sabadoCheckBox.setGeometry(QtCore.QRect(30, 180, 70, 17))
        self.sabadoCheckBox.setObjectName(_fromUtf8("sabadoCheckBox"))
        self.aceptarBtn = QtGui.QPushButton(Form)
        self.aceptarBtn.setGeometry(QtCore.QRect(10, 240, 75, 23))
        self.aceptarBtn.setObjectName(_fromUtf8("aceptarBtn"))
        self.cancelarBtn = QtGui.QPushButton(Form)
        self.cancelarBtn.setGeometry(QtCore.QRect(90, 240, 75, 23))
        self.cancelarBtn.setObjectName(_fromUtf8("cancelarBtn"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.aceptarBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.aceptar)
        QtCore.QObject.connect(self.cancelarBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.cancelar)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.diasGroupBox.setTitle(_translate("Form", "Días de la semana ", None))
        self.lunesCheckBox.setText(_translate("Form", "Lunes", None))
        self.martesCheckBox.setText(_translate("Form", "Martes", None))
        self.miercolesCheckBox.setText(_translate("Form", "Miércoles", None))
        self.juevesCheckBox.setText(_translate("Form", "Jueves", None))
        self.viernesCheckBox.setText(_translate("Form", "Viernes", None))
        self.sabadoCheckBox.setText(_translate("Form", "Sábado", None))
        self.aceptarBtn.setText(_translate("Form", "Aceptar", None))
        self.cancelarBtn.setText(_translate("Form", "Cancelar", None))

