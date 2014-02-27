# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EscogerRegistro.ui'
#
# Created: Sun Feb 23 23:28:41 2014
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
        Form.resize(838, 698)
        Form.setBaseSize(QtCore.QSize(0, -1))
        self.aceptarBtn = QtGui.QPushButton(Form)
        self.aceptarBtn.setGeometry(QtCore.QRect(20, 660, 75, 23))
        self.aceptarBtn.setObjectName(_fromUtf8("aceptarBtn"))
        self.registroTable = QtGui.QTableView(Form)
        self.registroTable.setGeometry(QtCore.QRect(20, 60, 791, 581))
        self.registroTable.setSortingEnabled(True)
        self.registroTable.setObjectName(_fromUtf8("registroTable"))
        self.filtroTxt = QtGui.QLineEdit(Form)
        self.filtroTxt.setGeometry(QtCore.QRect(62, 20, 131, 20))
        self.filtroTxt.setObjectName(_fromUtf8("filtroTxt"))
        self.tipoFiltroComboBox = QtGui.QComboBox(Form)
        self.tipoFiltroComboBox.setGeometry(QtCore.QRect(210, 20, 141, 22))
        self.tipoFiltroComboBox.setObjectName(_fromUtf8("tipoFiltroComboBox"))
        self.filtroLbl = QtGui.QLabel(Form)
        self.filtroLbl.setGeometry(QtCore.QRect(20, 20, 46, 13))
        self.filtroLbl.setObjectName(_fromUtf8("filtroLbl"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.aceptarBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.aceptar)
        QtCore.QObject.connect(self.filtroTxt, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), Form.actualizarFiltro)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Sistema Informacion Crece", None))
        self.aceptarBtn.setText(_translate("Form", "Aceptar", None))
        self.filtroLbl.setText(_translate("Form", "Filtro:", None))

