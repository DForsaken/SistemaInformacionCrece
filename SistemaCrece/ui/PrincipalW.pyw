#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys
import AgregarAreaW, AgregarPersonaW, InicioW, AgregarDonadorW, AgregarClasificacionW, CursosW
import AgregarViaDonacionW, AgregarEscuelaW 
from tableUtilities import tableUtilities
from Principal import Ui_MainWindow
from PyQt4.QtCore import pyqtSignal
from ui.AgregarEscuelaW import AgregarEscuela
from ui.comboBoxUtilities import comboBoxUtilities
import writeXls


class Principal(QtGui.QMainWindow):

    peticion = pyqtSignal()
    closed = pyqtSignal()

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Sistema Crece")
        self.args = []
        self.cursos = None
        self.cursosVentanaActiva = False
        self.filasAActualizar = []
        self.intIdx = []
        self.floatIdx = []
        self.ultimoProcVer = ""
        self.ultimoTipoPersonaVer = ""
        self.dataTypeFlag = 0
        self.formularioActivo = None
        self.estaActualizando = False
        # 0 for string
        # 1 for table
        # 2 for combobox
        self.tableUtilities = tableUtilities()
        self.tableUtilities.hiddenCols = []
        self.permisos = -1
        self.usuario = ""
        self.inicioActivo = False
        self.model = QtGui.QStandardItemModel(self)
        self.proxy = QtGui.QSortFilterProxyModel(self)
        self.comboBoxUtilities = comboBoxUtilities()
        self.clipboard = QtGui.QApplication.clipboard()
        self.inicio()
        
    def definirUsuarioPermisos(self, app):
        self.usuario = app.usuario
        self.permisos = app.permisos
        self.inicioActivo = False
        self.aplicarPoliticasPermisos()
        
    def aplicarPoliticasPermisos(self):
        if self.permisos == 2 or self.permisos == 3 or self.permisos == 4 or self.permisos == 5  or self.permisos == 6:
            self.ui.actionAgregarEmpleado.setVisible(False)
            self.ui.actionVerEmpleado.setVisible(False)
            if self.permisos != 4:
                self.ui.menuAgregarDonador.menuAction().setVisible(False)
            self.ui.actionAgregarArea.setVisible(False)
        if self.permisos == 5  or self.permisos == 6:
            if self.permisos == 5:
                self.ui.menuDonador.menuAction().setVisible(False)
            if self.permisos == 6:
                self.ui.menuAgregar.menuAction().setVisible(False)
            self.ui.actionAgregarInstitucion.setVisible(False)
            self.ui.menuAgregarDonador.menuAction().setVisible(False)
            self.ui.actionAgregarVoluntario.setVisible(False)
            self.ui.menuEstudiante.menuAction().setVisible(False)
        print "Permisos ", self.permisos
                
        
    def inicio(self):
        self.formularioActivo = InicioW.Inicio(self)
        self.formularioActivo.closed.connect(self.show)
        self.formularioActivo.peticion.connect(lambda:self.procesarPeticion(self.formularioActivo))
        self.formularioActivo.obtenerInfo.connect(lambda:self.definirUsuarioPermisos(self.formularioActivo))
        self.formularioActivo.exitApp.connect(self.close)
        self.formularioActivo.show()
        self.hide()
        self.inicioActivo = True

    def agregarArea(self):
        if self.permisos == 1:
            self.tableUtilities.editableCells = True
        self.formularioActivo = AgregarAreaW.AgregarArea(self)
        self.formularioActivo.closed.connect(self.show)
        self.formularioActivo.agregar.connect(lambda:self.procesarPeticion(self.formularioActivo))
        self.formularioActivo.show()
        self.hide()
           
    def agregarEmpleado(self):
        #mismo formulario que persona solo que agregar atributos faltantes en campos temp
        self.formularioActivo = AgregarPersonaW.AgregarPersona("Empleado", self )
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

    def agregarVoluntario(self):
        #mismo formulario que persona solo que agregar atributos faltantes en campos temp
        self.formularioActivo = AgregarPersonaW.AgregarPersona("Voluntario", self )
        self.formularioActivo.closed.connect(self.show)
        self.formularioActivo.peticion.connect(lambda:self.procesarPeticion(self.formularioActivo))
        self.formularioActivo.agregar.connect(lambda:self.procesarPeticion(self.formularioActivo))
        self.formularioActivo.show()
        self.hide()
        self.formularioActivo.llenarComboBox()

    def agregarAlumno(self):
        #mismo formulario que persona solo que agregar atributos faltantes en campos temp
        self.formularioActivo = AgregarPersonaW.AgregarPersona("Alumno", self )
        self.formularioActivo.closed.connect(self.show)
        self.formularioActivo.peticion.connect(lambda:self.procesarPeticion(self.formularioActivo))
        self.formularioActivo.agregar.connect(lambda:self.procesarPeticion(self.formularioActivo))
        self.formularioActivo.show()
        self.hide()
        self.formularioActivo.llenarComboBox()
            
    def agregarDonador(self):
        self.formularioActivo = AgregarDonadorW.AgregarDonador(self)
        self.formularioActivo.closed.connect(self.show)
        self.formularioActivo.peticion.connect(lambda:self.procesarPeticion(self.formularioActivo))
        self.formularioActivo.agregar.connect(lambda:self.procesarPeticion(self.formularioActivo))
        self.formularioActivo.show()
        self.hide()
        self.formularioActivo.llenarComboBox()

    def agregarClasificacion(self):
        self.formularioActivo = AgregarClasificacionW.AgregarClasificacion(self)
        self.formularioActivo.closed.connect(self.show)
        self.formularioActivo.agregar.connect(lambda:self.procesarPeticion(self.formularioActivo))
        self.formularioActivo.show()
        self.hide() 
        
    def agregarViaDonacion(self):
        self.formularioActivo = AgregarViaDonacionW.AgregarViaDonacion(self)
        self.formularioActivo.closed.connect(self.show)
        self.formularioActivo.agregar.connect(lambda:self.procesarPeticion(self.formularioActivo))
        self.formularioActivo.show()
        self.hide()  
        
    def agregarInstitucion(self):
        self.formularioActivo = AgregarEscuelaW.AgregarEscuela(self)
        self.formularioActivo.closed.connect(self.show)
        self.formularioActivo.agregar.connect(lambda:self.procesarPeticion(self.formularioActivo))
        self.formularioActivo.peticion.connect(lambda:self.procesarPeticion(self.formularioActivo))
        self.formularioActivo.show()
        self.hide() 
        self.formularioActivo.llenarComboBox()

    def verEmpleado(self):
        self.dataTypeFlag = 1
        self.tableUtilities.hiddenCols = []
        if self.permisos == 1:
            self.tableUtilities.editableCells = True
            self.ui.ActualizarBtn.show()
        else:
            self.tableUtilities.editableCells = False
            self.ui.ActualizarBtn.hide()
        self.procesarPeticionVer(["verEmpleado","","tabla"])    
        
    def verNino(self):
        self.dataTypeFlag = 1
        self.tableUtilities.hiddenCols = [17,18]
        if self.permisos == 1 or self.permisos == 2 or self.permisos == 3 or self.permisos == 4:
            self.tableUtilities.editableCells = True
            self.ui.ActualizarBtn.show()
        else:
            self.tableUtilities.editableCells = False
            self.ui.ActualizarBtn.hide()
        self.procesarPeticionVer(["verNino","","tabla"])
        
    def verAdulto(self):
        self.dataTypeFlag = 1
        self.tableUtilities.hiddenCols = [17,18]
        if self.permisos == 1 or self.permisos == 2 or self.permisos == 3 or self.permisos == 4:
            self.tableUtilities.editableCells = True
            self.ui.ActualizarBtn.show()
        else:
            self.tableUtilities.editableCells = False
            self.ui.ActualizarBtn.hide()
        self.procesarPeticionVer(["verAdulto","","tabla"])
                
    def verPracticante(self):
        self.dataTypeFlag = 1
        self.tableUtilities.hiddenCols = []
        if self.permisos == 1 or self.permisos == 2 or self.permisos == 3 or self.permisos == 4:
            self.tableUtilities.editableCells = True
            self.ui.ActualizarBtn.show()
        else:
            self.tableUtilities.editableCells = False
            self.ui.actualizarBtn.hide()
        self.procesarPeticionVer(["verPracticante","","tabla"])
        
    def verPrestador(self):
        self.dataTypeFlag = 1
        self.tableUtilities.hiddenCols = []
        if self.permisos == 1 or self.permisos == 2 or self.permisos == 3 or self.permisos == 4:
            self.tableUtilities.editableCells = True
            self.ui.ActualizarBtn.show()
        else:
            self.tableUtilities.editableCells = False
            self.ui.actualizarBtn.hide()
        self.procesarPeticionVer(["verPrestador","","tabla"])

    def desactivarVentanaCursos(self):
        self.show()
        self.cursosVentanaActiva = False

    def verCurso(self):
        self.tableUtilities.hiddenCols = []
        if self.cursos == None:
            print "No Existe Curso"
            self.cursos = CursosW.Curso(self)
            self.cursos.closed.connect(self.desactivarVentanaCursos)
            self.cursos.peticion.connect(self.procesarPeticionCursosVer)
        else:
            print "Existe Curso"
        self.cursos.show()
        self.cursosVentanaActiva = True
        self.cursos.usuario = self.usuario
        self.cursos.permisos = self.permisos
        self.cursos.aplicarPoliticasPermisos()
        self.hide() 
        
    def verInstitucion(self):
        self.dataTypeFlag = 1
        self.tableUtilities.hiddenCols = []
        if self.permisos == 1 or self.permisos == 2 or self.permisos == 3 or self.permisos == 4:
            self.tableUtilities.editableCells = True
            self.ui.ActualizarBtn.show()
        else:
            self.tableUtilities.editableCells = False
            self.ui.ActualizarBtn.hide()
        self.procesarPeticionVer(["verEscuela","","tabla"])
        return None

    def verDonador(self):
        self.dataTypeFlag = 1
        self.tableUtilities.hiddenCols = []
        if self.permisos == 1 or self.permisos == 4:
            self.tableUtilities.editableCells = True
            self.ui.ActualizarBtn.show()
        else:
            self.tableUtilities.editableCells = False
            self.ui.ActualizarBtn.hide()
        self.procesarPeticionVer(["verInstitucion","","tabla"])

    def verVoluntario(self):
        self.dataTypeFlag = 1
        self.tableUtilities.hiddenCols = [17,18]
        if self.permisos == 1 or self.permisos == 2 or self.permisos == 3 or self.permisos == 4:
            self.tableUtilities.editableCells = True
            self.ui.ActualizarBtn.show()
        else:
            self.tableUtilities.editableCells = False
            self.ui.ActualizarBtn.hide()
        self.procesarPeticionVer(["verVoluntario","","tabla"])

    def verArea(self):
        '''
        args -> tupla 3 elementos
        args[0] = nombre procedimiento
        args[1] = argumentos
        args[2] = tipo de retorno (tabla, string, comboBox)
        ''' 
        self.dataTypeFlag = 1  
        self.tableUtilities.hiddenCols = [0]
        if self.permisos == 1:
            self.tableUtilities.editableCells = True
            self.ui.ActualizarBtn.show()
        else:
            self.tableUtilities.editableCells = False
            self.ui.ActualizarBtn.hide()
        self.procesarPeticionVer(["verArea","","tabla"])
        
    def actualizar(self):
        self.estaActualizando = True
        if self.ultimoProcVer and len(self.filasAActualizar) != 0:
            self.args[2] = "string"
            self.dataTypeFlag = 0
            cols = self.ui.tableWidgetInfo.model().columnCount()
            for fila in self.filasAActualizar:
                self.args[0] = self.ultimoProcVer.replace("ver", "actualiza")
                print "proc a llamar - ", self.args[0]
                self.args[1] = []
                for j in range(0,cols):
                    print "checando ," , fila, " - ", j
                    print self.ui.tableWidgetInfo.model().index(fila, j).data().toString()
                    tempVar = self.ui.tableWidgetInfo.model().index(fila, j).data().toString()
                    if j in self.intIdx:
                        tempVar = int(tempVar)
                    elif j in self.floatIdx:
                        tempVar = float(tempVar)
                    else:
                        if tempVar == "None":
                            tempVar = "0000-00-00"
                        else:
                            tempVar = str(tempVar)
                    self.args[1].append(tempVar)
                if fila == self.filasAActualizar[len(self.filasAActualizar)-1]:
                    self.estaActualizando = False
                self.procesarPeticionActualizar()
        self.verUltimaVista()
            
    def agregarFilaAActualizar(self, model):
        print model.row()
        if model.row() not in self.filasAActualizar:
            self.filasAActualizar.append(model.row())
        print "filas a actualizar ", self.filasAActualizar
    
    def verUltimaVista(self):
        if self.ultimoProcVer == "actualizaPersona":
            self.args[0] = "ver" + self.ultimoTipoPersonaVer
        else:
            self.args[0] = self.ultimoProcVer
        self.args[1] = ""
        self.args[2] = "tabla"
        self.dataTypeFlag = 1
        print "llamando vista ", self.ultimoProcVer
        self.procesarPeticionVer(self.args)
    
    def obtenerTabla(self, res):
        print res
        if res != None:
            if self.cursos != None and self.cursosVentanaActiva:
                self.cursos.obtenerTabla(res)
            elif self.inicioActivo:
                self.formularioActivo.verificarBD(res)
            else:
                if isinstance(res, basestring):
                    self.mostrarMensaje(res)
                else:
                    print "set hid ", self.tableUtilities.hiddenCols
                    self.hiddenCols = self.tableUtilities.hiddenCols
                    self.comboBoxUtilities.llenarComboBoxFiltro(res, self.ui.tipoFiltroComboBox, self.tableUtilities.hiddenCols)
                    self.tableUtilities.populateTable(res, self.ui.tableWidgetInfo, self.model, self.proxy)
                    self.ui.tableWidgetInfo.resizeColumnsToContents()
                    self.ui.tableWidgetInfo.resizeRowsToContents()
                    self.intIdx = self.tableUtilities.intIdx
                    self.floatIdx = self.tableUtilities.floatIdx
                    self.filasAActualizar = []
        else:
            print "Empty result set"
        
    def cambiarVistaTabla(self, res):
        print "cambiando vista"
        #self.ui.tableWidgetInfo = tablaNueva
        for row in range(0,len(res)):
            self.ui.tableWidgetInfo.insertRow(row)
            record = res[row]                 
            for column in range (0,len(record)):                        
                newitem = QtGui.QTableWidgetItem(str(record[column]))
                self.ui.tableWidgetInfo.setItem(row,column,newitem)
    
    def obtenerComboBox(self, res):
        print res
        if res != None:
            if self.cursos != None and self.cursosVentanaActiva:
                self.cursos.obtenerComboBox(res)
            else:
                if isinstance(res, basestring):
                    self.mostrarMensaje(res)
                else:
                    if self.formularioActivo != None: 
                        self.formularioActivo.obtenerComboBox(res)
        else:
            print "Empty result set"
    
    def procesarPeticion(self, app):    
        if len(app.args) > 0:
            self.args = app.args[:]
            self.dataTypeFlag = app.dataTypeFlag
            print self.peticion.emit()
            print "procesar peticion app"
            self.args = []

    def procesarPeticionActualizar(self):    
        self.peticion.emit()
        print "procesar peticion actualizar"
            
    def procesarPeticionVer(self, args):    
        if len(args) > 0:
            self.args = args[:]
            if "Nino" in args[0] or "Adulto" in args[0] or "Voluntario" in args[0]:
                self.ultimoTipoPersonaVer = args[0][3:]
                self.ultimoProcVer = "actualizaPersona"
            else:
                self.ultimoProcVer = args[0]
            print self.peticion.emit()
            print "procesar peticion ver"     
            print "set hid ", self.tableUtilities.hiddenCols    
    
    def procesarPeticionCursosVer(self):    
        self.args = self.cursos.args[:]
        self.dataTypeFlag = self.cursos.dataTypeFlag
        print "print - ", self.args
        self.peticion.emit()
        
    def mostrarMensaje(self, mensaje, tipoMensaje):   
        if self.cursos != None and self.cursosVentanaActiva:
            self.cursos.mostrarMensaje(mensaje, tipoMensaje)
            print "pase a cursos"
        elif self.inicioActivo:
            self.formularioActivo.mostrarMensaje(mensaje, tipoMensaje)
        elif tipoMensaje == 1:
            QtGui.QMessageBox.critical(self, 'Error !', mensaje, QtGui.QMessageBox.Ok)
        elif tipoMensaje == 0 and self.estaActualizando == False:
            print "mensaje en principal"
            QtGui.QMessageBox.information(self, "Mensaje", mensaje, QtGui.QMessageBox.Ok) 
            
    def copiar(self):
        indexes = self.ui.tableWidgetInfo.selectedIndexes()
        if indexes >= 1:
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
                strCopia += str(self.ui.tableWidgetInfo.model().
                                    index(indexes[i].row(), indexes[i].column()).data().toString())
                idxAnterior = indexes[i].row()
            temp = ""
            for i in headerIndexes:
                temp += str(self.ui.tipoFiltroComboBox.itemText(i)) + "\t"
            strCopia = temp + "\n" + strCopia 
            self.clipboard.setText(strCopia)
            
    def enviarExcell(self):
        indexes = self.ui.tableWidgetInfo.selectedIndexes()
        headers = [] 
        tiposData = []
        data = []
        for i in range(0,self.ui.tableWidgetInfo.model().rowCount()):
            tempData = []
            for j in range(0,self.ui.tableWidgetInfo.model().columnCount()):
                if j not in self.hiddenCols:
                    tempData.append(str(self.ui.tableWidgetInfo.model().
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
                 
    def actualizarFiltro(self):
        filterColumn = self.ui.tipoFiltroComboBox.currentIndex()
        filterString = QtCore.QRegExp(  self.ui.filtroTxt.text(),
                                        QtCore.Qt.CaseInsensitive,
                                        QtCore.QRegExp.RegExp
                                     )
        self.proxy.setFilterRegExp(filterString)
        self.proxy.setFilterKeyColumn(filterColumn)

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()
        

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    formularioActivo = Principal()
    formularioActivo.show()
    sys.exit(app.exec_())
