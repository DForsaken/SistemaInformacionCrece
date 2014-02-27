#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys
import AgregarCursoW, AgregarCausaFaltaW, EscogerRegistroW, AgregarPersonaW, EscogerDiasSemanaW
from Cursos import Ui_MainWindow
from PyQt4.QtCore import pyqtSignal
from ui.tableUtilities import tableUtilities
from comboBoxUtilities import comboBoxUtilities
import writeXls


class Curso(QtGui.QMainWindow):

    closed = pyqtSignal()
    peticion = pyqtSignal()

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Sistema Crece")
        self.args = []
        self.dataTypeFlag = 0
        # 0 for string
        # 1 for table
        # 2 for combobox
        self.debeEscoger = False
        self.procALlamar = ""
        self.extraArgs = []
        self.ultimosArgsVer = []
        self.formularioActivo = None
        self.PeticionAgregarPersonaCurso = 0
        self.filasAActualizar = []
        self.intIdx = []
        self.floatIdx = []
        self.ultimoProcVer = ""
        self.estaActualizando = False
        self.tableUtilities = tableUtilities()
        self.tableUtilities.hiddenCols = []
        self.permisos = -1
        self.usuario = ""
        self.clipboard = QtGui.QApplication.clipboard()
        self.model = QtGui.QStandardItemModel(self)
        self.proxy = QtGui.QSortFilterProxyModel(self)
        self.comboBoxUtilities = comboBoxUtilities()

    def aplicarPoliticasPermisos(self):
        self.ui.actionCausa_falta.setVisible(False)
        if self.permisos == 5 or self.permisos == 6:
            print "Permisos Crusos ", self.permisos
            self.ui.actionAgregaCurso.setVisible(False)
            self.ui.menuVoluntario.menuAction().setVisible(False)
            self.ui.menuAgregar.menuAction().setVisible(False)
            if self.permisos == 6:
                self.ui.menuAgregarAlumno.menuAction().setVisible(False)
            
        
    def ingresar(self):
        self.close()       

    def agregarCurso(self):
        self.formularioActivo = AgregarCursoW.AgregarCurso(self)
        self.formularioActivo.peticion.connect(lambda:self.procesarPeticion(self.formularioActivo))
        self.formularioActivo.agregar.connect(lambda:self.agregarCursoDiasSemana(
                                                        self.formularioActivo.args))
        self.formularioActivo.closed.connect(self.show)
        self.formularioActivo.show()
        self.hide()
        self.formularioActivo.llenarComboBox()
        
    def agregarCursoDiasSemana(self, args):
        self.formularioActivo.close()
        self.formularioActivo = EscogerDiasSemanaW.EscogerDiasSemana(self)
        self.formularioActivo.closed.connect(self.show)
        self.formularioActivo.agregar.connect(lambda:self.procesarPeticion(self.formularioActivo))
        self.formularioActivo.show()
        self.formularioActivo.inicializarArgs(args)    
        
    def agregarPracticanteCurso(self):  
        self.dataTypeFlag = 1
        self.PeticionAgregarPersonaCurso = 3
        self.debeEscoger = True
        self.procALlamar = "verPracticante"
        self.procesarPeticionVer(["verPersona", "", "tabla"])
        
    def agregarPrestadorCurso(self):  
        self.dataTypeFlag = 1
        self.PeticionAgregarPersonaCurso = 3
        self.debeEscoger = True
        self.procALlamar = "verPrestador"
        self.procesarPeticionVer(["verPersona", "", "tabla"])
        
    def agregarAlumnoCurso(self):
        self.procALlamar = "verAlumno"
        self.escogerR(4)   

    def agregarVoluntarioCurso(self):
        self.dataTypeFlag = 1
        self.PeticionAgregarPersonaCurso = 3
        self.debeEscoger = True
        self.procALlamar = "verVoluntario"
        self.procesarPeticionVer(["verPersona", "", "tabla"])

    def agregarCausaFaltaCurso(self):
        myapp = AgregarCausaFaltaW.AgregarCausaFalta(self)
        myapp.closed.connect(self.show)
        myapp.show()
        self.hide()

    def agregarAlumno(self):
        #mismo formulario que persona solo que agregar atributos faltantes en campos temp
        self.formularioActivo = AgregarPersonaW.AgregarPersona("Alumno", self )
        self.formularioActivo.closed.connect(self.show)
        self.formularioActivo.peticion.connect(lambda:self.procesarPeticion(self.formularioActivo))
        self.formularioActivo.agregar.connect(lambda:self.procesarPeticion(self.formularioActivo))
        self.formularioActivo.show()
        self.hide()
        self.formularioActivo.llenarComboBox()      
    
    def agregarVoluntario(self):
        #mismo formulario que persona solo que agregar atributos faltantes en campos temp
        self.formularioActivo = AgregarPersonaW.AgregarPersona("Voluntario", self )
        self.formularioActivo.closed.connect(self.show)
        self.formularioActivo.peticion.connect(lambda:self.procesarPeticion(self.formularioActivo))
        self.formularioActivo.agregar.connect(lambda:self.procesarPeticion(self.formularioActivo))
        self.formularioActivo.show()
        self.hide()
        self.formularioActivo.llenarComboBox()  
        
    def agregarPracticante(self):
        self.formularioActivo = AgregarPersonaW.AgregarPersona("Practicante", self )
        self.formularioActivo.closed.connect(self.show)
        self.formularioActivo.peticion.connect(lambda:self.procesarPeticion(self.formularioActivo))
        self.formularioActivo.agregar.connect(lambda:self.procesarPeticion(self.formularioActivo))
        self.formularioActivo.show()
        self.hide()
        self.formularioActivo.llenarComboBox() 
        
    def agregarPrestador(self):
        self.formularioActivo = AgregarPersonaW.AgregarPersona("Prestador", self )
        self.formularioActivo.closed.connect(self.show)
        self.formularioActivo.peticion.connect(lambda:self.procesarPeticion(self.formularioActivo))
        self.formularioActivo.agregar.connect(lambda:self.procesarPeticion(self.formularioActivo))
        self.formularioActivo.show()
        self.hide()
        self.formularioActivo.llenarComboBox() 
  
    def verPracticante(self):
        self.dataTypeFlag = 1
        if self.permisos == 1 or self.permisos == 2 or self.permisos == 3 or self.permisos == 4:
            self.tableUtilities.editableCells = True
            self.ui.actualizarBtn.show()
        else:
            self.tableUtilities.editableCells = False
            self.ui.actualizarBtn.hide()
        self.procesarPeticionVer(["verPracticante","","tabla"])
        
    def verPrestador(self):
        self.dataTypeFlag = 1
        if self.permisos == 1 or self.permisos == 2 or self.permisos == 3 or self.permisos == 4:
            self.tableUtilities.editableCells = True
            self.ui.actualizarBtn.show()
        else:
            self.tableUtilities.editableCells = False
            self.ui.actualizarBtn.hide()
        self.procesarPeticionVer(["verPrestador","","tabla"])

    def verCatalogoCursos(self):
        self.dataTypeFlag = 1
        self.tableUtilities.hiddenCols = [7]
        if self.permisos == 1 or self.permisos == 2 or self.permisos == 3 or self.permisos == 4:
            self.tableUtilities.editableCells = True
            self.ui.actualizarBtn.show()
        else:
            self.tableUtilities.editableCells = False
            self.ui.actualizarBtn.hide()
        self.procesarPeticionVer(["verCurso","","tabla"])

    def verAsistenciaAlumno(self):
        self.dataTypeFlag = 1
        if self.permisos == 6:
            self.tableUtilities.editableCells = False
            self.ui.actualizarBtn.hide()
        else:
            self.tableUtilities.editableCells = True
            self.ui.actualizarBtn.show()
        self.procALlamar = "verAsistenciaAlumno"
        self.escogerR(0)
        
    def verAsistenciaPracticante(self):
        self.dataTypeFlag = 1
        if self.permisos == 6:
            self.tableUtilities.editableCells = False
            self.ui.actualizarBtn.hide()
        else:
            self.tableUtilities.editableCells = True
            self.ui.actualizarBtn.show()
        self.procALlamar = "verAsistenciaPracticante"
        self.escogerR(0)
    
    def verAsistenciaPrestador(self):
        self.dataTypeFlag = 1
        if self.permisos == 6:
            self.tableUtilities.editableCells = False
            self.ui.actualizarBtn.hide()
        else:
            self.tableUtilities.editableCells = True
            self.ui.actualizarBtn.show()
        self.procALlamar = "verAsistenciaPrestador"
        self.escogerR(0)    
    

    def verVoluntarioCurso(self):
        self.dataTypeFlag = 1
        if self.permisos == 1 or self.permisos == 2 or self.permisos == 3 or self.permisos == 4:
            self.tableUtilities.editableCells = True
            self.ui.actualizarBtn.show()
        else:
            self.tableUtilities.editableCells = False
            self.ui.actualizarBtn.hide()
        self.procALlamar = "verCursoVoluntarioPorCurso"
        self.escogerR(0)

    def verPracticanteCurso(self):
        self.dataTypeFlag = 1
        if self.permisos == 1 or self.permisos == 2 or self.permisos == 3 or self.permisos == 4:
            self.tableUtilities.editableCells = True
            self.ui.actualizarBtn.show()
        else:
            self.tableUtilities.editableCells = False
            self.ui.actualizarBtn.hide()
        self.procALlamar = "verCursoPracticantePorCurso"
        self.escogerR(0)

    def verPrestadorCurso(self):
        self.dataTypeFlag = 1
        if self.permisos == 1 or self.permisos == 2 or self.permisos == 3 or self.permisos == 4:
            self.tableUtilities.editableCells = True
            self.ui.actualizarBtn.show()
        else:
            self.tableUtilities.editableCells = False
            self.ui.actualizarBtn.hide()
        self.procALlamar = "verCursoPrestadorPorCurso"
        self.escogerR(0)

    def verAlumnoCurso(self):    
        self.dataTypeFlag = 1
        if self.permisos == 1 or self.permisos == 2 or self.permisos == 3 or self.permisos == 4:
            self.tableUtilities.editableCells = True
            self.ui.actualizarBtn.show()
        else:
            self.tableUtilities.editableCells = False
            self.ui.actualizarBtn.hide()
        self.procALlamar = "verCursoAlumnoPorCurso"
        self.escogerR(0)

    def verVoluntario(self):
        self.dataTypeFlag = 1
        self.tableUtilities.hiddenCols = [17,18]
        if self.permisos == 1 or self.permisos == 2 or self.permisos == 3 or self.permisos == 4:
            self.tableUtilities.editableCells = True
            self.ui.actualizarBtn.show()
        else:
            self.tableUtilities.editableCells = False
            self.ui.actualizarBtn.hide()
        self.procesarPeticionVer(["verCursoVoluntario","","tabla"])
           
    def verAlumnos(self):
        self.dataTypeFlag = 1
        if self.permisos == 1 or self.permisos == 2 or self.permisos == 3 or self.permisos == 4:
            self.tableUtilities.editableCells = True
            self.ui.actualizarBtn.show()
        else:
            self.tableUtilities.editableCells = False
            self.ui.actualizarBtn.hide()
        self.procesarPeticionVer(["verCursoAlumno","","tabla"])

    def regresarACursos(self):
        self.show()
        self.formularioActivo.close()

    def actualizar(self):
        print "actualizar ", self.filasAActualizar
        self.estaActualizando = True
        if self.ultimoProcVer and len(self.filasAActualizar) != 0:
            self.args[2] = "string"
            self.dataTypeFlag = 0
            for fila in self.filasAActualizar:
                print "filas !! " , fila, " - ", len(self.filasAActualizar), " - ", self.filasAActualizar
                cols = self.ui.infoTableWidget.model().columnCount()
                self.args[0] = self.ultimoProcVer.replace("ver", "actualiza")
                print "proc a llamar - ", self.args[0]
                self.args[1] = []
                for j in range(0,cols):
                    print "checando ," , fila, " - ", j
                    print self.ui.infoTableWidget.model().index(fila, j).data().toString()
                    tempVar = self.ui.infoTableWidget.model().index(fila, j).data().toString()
                    if j in self.intIdx:
                        tempVar = int(tempVar)
                    elif j in self.floatIdx:
                        tempVar = float(tempVar)
                    else:
                        if tempVar == "None":
                            tempVar = "0000-00-00"
                        if tempVar == "":
                            tempVar = str("")
                        else:
                            tempVar = str(tempVar)
                    self.args[1].append(tempVar)
                print "tammmmmmmmmm ", len(self.filasAActualizar)
                if len(self.filasAActualizar) == 1 or fila == self.filasAActualizar[len(self.filasAActualizar)-1]:
                    self.estaActualizando = False
                if "PorCurso" in self.args[0]:
                    self.args[0] = self.args[0].replace("PorCurso", "") 
                self.procesarPeticionActualizar()
        self.verUltimaVista()
            
    def agregarFilaAActualizar(self, model):
        if model.row() not in self.filasAActualizar:
            print "agregando", model.row()
            self.filasAActualizar.append(model.row())
    
    def verUltimaVista(self):
        self.args[0] = self.ultimoProcVer
        if "Curso" in self.ultimoProcVer or "Asistencia" in self.ultimoProcVer  :
            self.args[1] = self.ultimosArgsVer
        else:
            self.args[1] = ""
        self.args[2] = "tabla"
        self.dataTypeFlag = 1
        print "llamando vista ", self.ultimoProcVer
        self.procesarPeticionVer(self.args)
    
    def obtenerTabla(self, res):
        print res
        if(res != None):
            if(len(res) != 0):
                if self.debeEscoger:
                    self.escogerRegistroW = None
                    self.escogerRegistroW = EscogerRegistroW.EscogerRegistro(self)
                    self.escogerRegistroW.definirTipo(False)
                    if self.PeticionAgregarPersonaCurso == 1 or self.PeticionAgregarPersonaCurso == 4 :
                        self.escogerRegistroW.agregar.connect(
                                            lambda:self.guardarArgsParaSiguienteProc(
                                                    self.escogerRegistroW.args)) 
                        if self.PeticionAgregarPersonaCurso == 4:
                            self.escogerRegistroW.diasSemana = True
                        self.PeticionAgregarPersonaCurso = 2                
                    elif self.PeticionAgregarPersonaCurso == 2:
                        self.escogerRegistroW.definirTipo(True)
                        self.escogerRegistroW.appendArgs(self.extraArgs)
                        #self.escogerRegistroW.closed.connect(self.hide)
                        if "Practicante" in self.procALlamar or "Prestador" in self.procALlamar:   
                            tempALlamar = "insertaCursoEstudiante"
                        else:
                            tempALlamar = self.procALlamar.replace("ver", "insertaCurso")
                        self.escogerRegistroW.agregar.connect(lambda:
                                         self.procesarPeticionVer([
                                                tempALlamar,
                                                        self.escogerRegistroW.args,"string"]))
                        self.dataTypeFlag = 0
                        self.debeEscoger = False      
                        self.PeticionAgregarPersonaCurso = 0            
                    elif self.PeticionAgregarPersonaCurso == 0:
                        #self.escogerRegistroW.closed.connect(self.show)
                        self.escogerRegistroW.agregar.connect(lambda:
                                         self.procesarPeticionVer([self.procALlamar,
                                                                   self.escogerRegistroW.args,"tabla"]))
                        self.debeEscoger = False            
                        self.extraArgs = []      
                    elif self.PeticionAgregarPersonaCurso == 3:
                        self.escogerRegistroW.definirTipo(True)
                        self.escogerRegistroW.agregar.connect(lambda:self.escogerR(1))
                        #self.escogerRegistroW.closed.connect(self.hide)
                    self.escogerRegistroW.closed.connect(self.show)
                    self.escogerRegistroW.show()
                    self.escogerRegistroW.llenarTabla(res)
                    self.hide()
                else:
                    if isinstance(res, basestring):
                        QtGui.QMessageBox.critical(self, 'Error !', res, QtGui.QMessageBox.Ok)
                    else:
                        self.hiddenCols = self.tableUtilities.hiddenCols
                        self.comboBoxUtilities.llenarComboBoxFiltro(res, self.ui.tipoFiltroComboBox, self.tableUtilities.hiddenCols)
                        self.tableUtilities.populateTable(res, self.ui.infoTableWidget, self.model, self.proxy)
                        self.ui.infoTableWidget.resizeColumnsToContents()
                        self.ui.infoTableWidget.resizeRowsToContents()
                        self.intIdx = self.tableUtilities.intIdx
                        self.floatIdx = self.tableUtilities.floatIdx
                    print 'llenando tabla'
                print "tabla lista"
            else:
                print "tabla vacia"        
        else:
            print "Empty result set"
        
    def escogerR(self, val):
        if self.PeticionAgregarPersonaCurso == 3 or self.PeticionAgregarPersonaCurso == 4:
            self.extraArgs = self.escogerRegistroW.args
            if self.PeticionAgregarPersonaCurso == 4:
                self.PeticionAgregarPersonaCurso = 1
            print "extra args escoger -", self.extraArgs
        else:
            self.extraArgs = []
        self.PeticionAgregarPersonaCurso = val
        self.debeEscoger = True
        self.verCatalogoCursos()    

    def guardarArgsParaSiguienteProc(self, args):
        if len(self.extraArgs) == 0:
            self.extraArgs = args
        else:
            print "args solos ", args
            for i in args:
                self.extraArgs.append(i)
        print "extra args", self.extraArgs
        self.procesarPeticionVer([self.procALlamar,"","tabla"])
    
    def cambiarVistaTabla(self, res):
        print "cambiando vista"
        #self.ui.infoTableWidget = tablaNueva
        for row in range(0,len(res)):
            self.ui.infoTableWidget.insertRow(row)
            record = res[row]                 
            for column in range (0,len(record)):                        
                newitem = QtGui.QTableWidgetItem(str(record[column]))
                self.ui.infoTableWidget.setItem(row,column,newitem)
    
    def obtenerComboBox(self, res):
        print res
        if res != None:
            if isinstance(res, basestring):
                self.mostrarMensaje(res)    
            else:
                if self.formularioActivo != None: 
                    self.formularioActivo.obtenerComboBox(res)
        else:
            print "Empty result set"

    def mostrarMensaje(self, mensaje, tipoMensaje):    
        if tipoMensaje == 1:
            QtGui.QMessageBox.critical(self, 'Error !', mensaje, QtGui.QMessageBox.Ok)
        elif tipoMensaje == 0 and self.estaActualizando == False:
            QtGui.QMessageBox.information(self, "Mensaje", mensaje, QtGui.QMessageBox.Ok) 

    def procesarPeticion(self, app):    
        if len(app.args) > 0:
            self.args = app.args[:]
            self.dataTypeFlag = app.dataTypeFlag
            self.ultimosArgsVer = app.args[1]
            self.peticion.emit()
            print self.args
            print "CursosW procesar peticion app"
    
    def procesarPeticionActualizar(self):    
        self.peticion.emit()
        print "procesar peticion actualizar"
            
    def procesarPeticionVer(self, args):    
        if len(args) > 0:
            print "procesar peticion ver cursos ", args[0]   
            self.args = args[:]
            self.filasAActualizar = []
            if not "Curso" in args[0] and "Voluntario" in args[0]:
                self.ultimoTipoPersonaVer = args[0][3:]
                self.ultimoProcVer = "actualizaPersona"
            else:
                self.ultimoProcVer = args[0]
            self.ultimosArgsVer = args[1]
            print self.peticion.emit()
            
    def actualizarFiltro(self):
        filterColumn = self.ui.tipoFiltroComboBox.currentIndex()
        filterString = QtCore.QRegExp(  self.ui.busquedaTxt.text(),
                                        QtCore.Qt.CaseInsensitive,
                                        QtCore.QRegExp.RegExp)
        self.proxy.setFilterRegExp(filterString)
        self.proxy.setFilterKeyColumn(filterColumn)

    def copiar(self):
        indexes = self.ui.infoTableWidget.selectedIndexes()
        headerIndexes = [] 
        strCopia = ""
        idxAnterior = indexes[0].row()
        indexes.sort()
        for i in range(0,len(indexes)):
            if indexes[i].column() not in headerIndexes:
                headerIndexes.append(indexes[i].column())
            if i != 0 and idxAnterior == indexes[i].row():
                strCopia += "\t"
            else:
                strCopia += "\n"
            strCopia += str(self.ui.infoTableWidget.model().
                                index(indexes[i].row(), indexes[i].column()).data().toString())
            idxAnterior = indexes[i].row()
        temp = ""
        for i in headerIndexes:
            temp += str(self.ui.tipoFiltroComboBox.itemText(i)) + "\t"
        strCopia = temp + "\n" + strCopia 
        self.clipboard.setText(strCopia)
        
    def enviarExcell(self):
        headers = [] 
        tiposData = []
        data = []
        for i in range(0,self.ui.infoTableWidget.model().rowCount()):
            tempData = []
            for j in range(0,self.ui.infoTableWidget.model().columnCount()):
                if j not in self.hiddenCols:
                    tempData.append(str(self.ui.infoTableWidget.model().
                                index(i,j).data().toString()).encode("UTF-8"))
            data.append(tempData)
        for i in range(0,self.ui.tipoFiltroComboBox.count()):
            headers.append(str(self.ui.tipoFiltroComboBox.itemText(i)).encode("UTF-8"))
            tiposData.append('text'.encode("UTF-8"))
               
        files_types = "Libro de Excel 97-2003 (*.xls)"
        fileName, filter = QtGui.QFileDialog.getSaveFileNameAndFilter(self, 'Open file', '', files_types)   
        wxls = writeXls.writeXls()
        print "mandando a excell ", str(len(data[0])), " - ", str(len(tiposData)), " - ", str(len(headers))
        print data[0]
        try:
            wxls.write_xls(str(fileName).encode("UTF-8"), 'Libro 1'.encode("UTF-8"), headers, data, tiposData) 
            self.mostrarMensaje("Reporte realizado con exito !!", 0)
        except Exception, e:
            self.mostrarMensaje("No se pudo realizar el reporte", 1)
            print e

           
    def closeEvent(self, event):
        self.closed.emit()  
        event.accept()



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Curso()
    myapp.show()
    sys.exit(app.exec_())