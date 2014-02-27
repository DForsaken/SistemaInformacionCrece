#! /usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import types

class tableUtilities:
    
    def __init__(self):
        self.hiddenCols = []
        self.editableCells = False
        
    def populateTable(self, res, table, model, proxy):
        if len(res) != 0 :
            print "escod ", self.hiddenCols
            self.intIdx = []
            self.floatIdx = []
            rows = len(res)-1
            cols = len(res[0])
            model.setRowCount(rows)
            model.setColumnCount(cols)
            headers = QtCore.QStringList() 
            for i in range(0,cols):
                headers.append(QtCore.QString(res[0][i]))
            model.setHorizontalHeaderLabels(headers)
            for i in range(0,rows):
                for j in range (0,cols):      
                    item = res[i+1][j]              
                    if isinstance(item, int):
                        self.intIdx.append(j)
                    elif isinstance(item, float):
                        self.floatIdx.append(j)
                    item = str(item)
                    item = QtGui.QStandardItem(item)
                    itemFlags = (QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled )
                    if self.editableCells:
                        itemFlags = itemFlags | QtCore.Qt.ItemIsEditable
                    item.setFlags(itemFlags)
                    model.setItem(i,j,item)
            proxy.setSourceModel(model)
            table.setModel(proxy)
            for i in range(0,rows):
                for j in range (0,cols):  
                    if j in self.hiddenCols:
                        table.setColumnHidden(j, True)
                        print "Escondi  a ", j
            print "tabla lista"
            self.hiddenCols = []
        else:
            print "tabla vacia"
               