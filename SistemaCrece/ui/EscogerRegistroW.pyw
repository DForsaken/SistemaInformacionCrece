#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import pyqtSignal
from escogerRegistro import Ui_Form
from PyQt4 import QtCore, QtGui
from ui.tableUtilities import tableUtilities
import comboBoxUtilities

class EscogerRegistro(QtGui.QMainWindow):

    closed = pyqtSignal()
    agregar = pyqtSignal()

    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Selecciona un registro !!")
        self.tableUtilities = tableUtilities()
        self.args = []
        self.diasSemana = False
        self.model = QtGui.QStandardItemModel(self)
        self.proxy = QtGui.QSortFilterProxyModel(self)
        self.comboBoxUtilities = comboBoxUtilities.comboBoxUtilities()
        self.aceptar = True


    def llenarTabla(self, res):
        print "Llenando ", res
        self.comboBoxUtilities.llenarComboBoxFiltro(res, self.ui.tipoFiltroComboBox, [])
        self.tableUtilities.populateTable(res, self.ui.registroTable, self.model, self.proxy)
        self.ui.registroTable.resizeColumnsToContents()
        self.ui.registroTable.resizeRowsToContents()
    
    def appendArgs(self, args):
        for i in args:
            self.args.append(i)
    
    def definirTipo(self, esPersona):
        self.esPersona = esPersona
    
    def obtenerFilaSeleccionada(self):
        for i in range(0,self.ui.registroTable.model().rowCount()):
            for j in range(0,self.ui.registroTable.model().columnCount()):
                indexes = self.ui.registroTable.selectedIndexes()
                if len(indexes) == 0 or len(indexes) > 1:
                    self.mostrarMensaje("Solo selecciona un registro !")
                    return
                else:
                    for item in indexes:
                        if indexes[0].row() == i:
                            return indexes[0].row()
        return -1        
    
    def mostrarMensaje(self, mensaje):   
        QtGui.QMessageBox.critical(self, 'Error !', mensaje, QtGui.QMessageBox.Ok)
        
    # 1 2 3 7
    def aceptar(self):
        filaSeleccionada = self.obtenerFilaSeleccionada()
        print 'filaSeleccionada - ', filaSeleccionada
        if filaSeleccionada == -1:
            self.mostrarMensaje('Debes seleccionar primero un elemento')
        else:
            self.aceptar = True
            self.args.append(str(self.ui.registroTable.model().index(filaSeleccionada, 0).data().toString()))
            self.args.append(str(self.ui.registroTable.model().index(filaSeleccionada, 1).data().toString()))
            self.args.append(str(self.ui.registroTable.model().index(filaSeleccionada, 2).data().toString()))
            if not(self.esPersona): #tipo Cursos
                self.args.append(str(self.ui.registroTable.model().index(filaSeleccionada, 6).data().toString()))
                if self.diasSemana:
                    self.args.append(str(self.ui.registroTable.model().index(filaSeleccionada, 3).data().toString()))
                    self.args.append(str(self.ui.registroTable.model().index(filaSeleccionada, 7).data().toString()))
            self.agregar.emit()
            self.close()
            
    def actualizarFiltro(self):
        filterColumn = self.ui.tipoFiltroComboBox.currentIndex()
        filterString = QtCore.QRegExp(  self.ui.filtroTxt.text(),
                                        QtCore.Qt.CaseInsensitive,
                                        QtCore.QRegExp.RegExp
                                        )
        self.proxy.setFilterRegExp(filterString)
        self.proxy.setFilterKeyColumn(filterColumn)

             
    def closeEvent(self, event):
        if self.aceptar:
            self.closed.emit()
        event.accept()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = EscogerRegistro()
    myapp.show()
    sys.exit(app.exec_())
    
    
    