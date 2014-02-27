'''
Created on 05/02/2014

@author: The Forsaken
'''
from PyQt4 import QtGui, QtCore

class QComboBoxWrapper(QtGui.QComboBox):
    
    
    def __init__(self, *args, **kwargs):
        QtGui.QComboBox.__init__(self, *args, **kwargs)
        self.dictData = {}
        self.counter = 0
        
    def getIdFromCurrentItem(self):
        a = self.dictData.get(self.currentIndex())
        print 'resultado ', a
        return a
        
    def setIdFromNewItem(self, value, id):
        print 'val ', value, ' id ', id
        self.dictData.update({self.counter:id})
        self.addItem(value, QtCore.QVariant(self.counter))
        self.counter += 1
        
        