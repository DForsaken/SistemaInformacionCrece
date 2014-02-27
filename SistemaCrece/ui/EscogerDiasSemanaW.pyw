'''
Created on 14/02/2014

@author: The Forsaken
'''
import sys
from PyQt4.QtCore import pyqtSignal
from EscogerDiasSemana import Ui_Form
from PyQt4 import QtCore, QtGui

class EscogerDiasSemana(QtGui.QMainWindow):

    closed = pyqtSignal()
    agregar = pyqtSignal()

    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Sistema Crece")
        self.args = ["",[],""]
        self.dataTypeFlag = 0   
        # 0 for string
        # 1 for table
        # 2 for combobox
        
    def inicializarArgs(self, args):
        self.args = args
        
    def aceptar(self):
        if self.ui.lunesCheckBox.isChecked():
            self.args[1].append(0)
        else:
            self.args[1].append(-1)
        if self.ui.martesCheckBox.isChecked():
            self.args[1].append(1)
        else:
            self.args[1].append(-1)
        if self.ui.miercolesCheckBox.isChecked():
            self.args[1].append(2)
        else:
            self.args[1].append(-1)
        if self.ui.juevesCheckBox.isChecked():
            self.args[1].append(3)
        else:
            self.args[1].append(-1)
        if self.ui.viernesCheckBox.isChecked():
            self.args[1].append(4)
        else:
            self.args[1].append(-1)
        if self.ui.sabadoCheckBox.isChecked():
            self.args[1].append(5)
        else:
            self.args[1].append(-1)
        print " escogiendo dias"
        self.agregar.emit()
        self.cancelar()

    def cancelar(self):
        self.close()

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = EscogerDiasSemana()
    myapp.show()
    sys.exit(app.exec_())