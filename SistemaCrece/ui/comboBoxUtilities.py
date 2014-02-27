'''
Created on 04/02/2014

@author: The Forsaken
'''

from PyQt4 import QtCore, QtGui
import sys

class comboBoxUtilities():
    
    def __init__(self):
        self.idIdx = []
        self.dataIdx = []
    
    def populateComboBox(self, comboBox, res):
        self.id = []
        self.dataStr = []
        if len(res) != 0 :
            rows = len(res)
            for i in range(1, rows):
                temp = []
                for j in self.idIdx:
                    print 'res ', res[i][j]
                    temp.append(res[i][j])
                self.id.append(temp)
                tempStr = ""
                for j in self.dataIdx:
                    print i, " - ", j , " - ", res[i][j]
                    tempStr += str(res[i][j]) + " "
                self.dataStr.append(tempStr)
            for i in range(0, len(self.dataStr)):
                comboBox.setIdFromNewItem(self.dataStr[i], self.id[i])
                print self.id[i], ' - ', self.dataStr[i] 
                
    def setIndex(self, type):
        if type == "Colonia":
            self.dataIdx = [0,1]
            self.idIdx = [0]
        elif type == "GradoEscolar":
            self.dataIdx = [0,1]
            self.idIdx = [0,1]
        elif type == "Area":
            self.dataIdx = [1]
            self.idIdx = [0]
        elif type == "Permiso":
            self.dataIdx = [1]
            self.idIdx = [1]
        elif type == "Escuela":
            self.dataIdx = [0,2]
            self.idIdx = [0,2]
        elif type == "Puesto":
            self.dataIdx = [0,1]
            self.idIdx = [0,1]
        elif type == "Clasificacion":
            self.dataIdx = [1]
            self.idIdx = [0]
        elif type == "ViaDonacion":
            self.dataIdx = [1]
            self.idIdx = [0]
        elif type == "Curso":
            self.dataIdx = [0,1,3,6]
            self.idIdx = [0,1,3,6]
        elif type == "Persona":
            self.dataIdx = [0,1,2]
            self.idIdx = [0,1,2]
        
    def llenarComboBoxFiltro(self, res, comboBox, colsHidde):
        if len(res) != 0 :
            cols = len(res[0])
            strList = []
            for i in range(0,cols):
                if not(i in colsHidde):
                    strList.append(str(res[0][i]))
            comboBox.clear()
            comboBox.addItems(strList)           
        
        
        
        
        
        
        
    