# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Principal.ui'
#
# Created: Wed Feb 26 21:14:54 2014
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1121, 771)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.dockWidgetInfo = QtGui.QDockWidget(self.centralWidget)
        self.dockWidgetInfo.setGeometry(QtCore.QRect(10, 0, 1091, 711))
        self.dockWidgetInfo.setAutoFillBackground(True)
        self.dockWidgetInfo.setFloating(False)
        self.dockWidgetInfo.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
        self.dockWidgetInfo.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.dockWidgetInfo.setObjectName(_fromUtf8("dockWidgetInfo"))
        self.dockWidgetContents_3 = QtGui.QWidget()
        self.dockWidgetContents_3.setObjectName(_fromUtf8("dockWidgetContents_3"))
        self.filtroLbl = QtGui.QLabel(self.dockWidgetContents_3)
        self.filtroLbl.setGeometry(QtCore.QRect(10, 20, 46, 13))
        self.filtroLbl.setObjectName(_fromUtf8("filtroLbl"))
        self.filtroTxt = QtGui.QLineEdit(self.dockWidgetContents_3)
        self.filtroTxt.setGeometry(QtCore.QRect(50, 20, 113, 20))
        self.filtroTxt.setObjectName(_fromUtf8("filtroTxt"))
        self.ActualizarBtn = QtGui.QPushButton(self.dockWidgetContents_3)
        self.ActualizarBtn.setGeometry(QtCore.QRect(1000, 20, 75, 23))
        self.ActualizarBtn.setObjectName(_fromUtf8("ActualizarBtn"))
        self.tipoFiltroComboBox = QtGui.QComboBox(self.dockWidgetContents_3)
        self.tipoFiltroComboBox.setGeometry(QtCore.QRect(190, 20, 121, 22))
        self.tipoFiltroComboBox.setObjectName(_fromUtf8("tipoFiltroComboBox"))
        self.tableWidgetInfo = QtGui.QTableView(self.dockWidgetContents_3)
        self.tableWidgetInfo.setGeometry(QtCore.QRect(10, 60, 1071, 611))
        self.tableWidgetInfo.setObjectName(_fromUtf8("tableWidgetInfo"))
        self.copiarBtn = QtGui.QPushButton(self.dockWidgetContents_3)
        self.copiarBtn.setGeometry(QtCore.QRect(900, 20, 75, 23))
        self.copiarBtn.setObjectName(_fromUtf8("copiarBtn"))
        self.dockWidgetInfo.setWidget(self.dockWidgetContents_3)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1121, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuUsuario = QtGui.QMenu(self.menuBar)
        self.menuUsuario.setObjectName(_fromUtf8("menuUsuario"))
        self.menuAgregar = QtGui.QMenu(self.menuUsuario)
        self.menuAgregar.setObjectName(_fromUtf8("menuAgregar"))
        self.menuEstudiante = QtGui.QMenu(self.menuAgregar)
        self.menuEstudiante.setObjectName(_fromUtf8("menuEstudiante"))
        self.menuVer = QtGui.QMenu(self.menuUsuario)
        self.menuVer.setObjectName(_fromUtf8("menuVer"))
        self.menuEstudiante_2 = QtGui.QMenu(self.menuVer)
        self.menuEstudiante_2.setObjectName(_fromUtf8("menuEstudiante_2"))
        self.menuCursos = QtGui.QMenu(self.menuBar)
        self.menuCursos.setObjectName(_fromUtf8("menuCursos"))
        self.menuInstituciones = QtGui.QMenu(self.menuBar)
        self.menuInstituciones.setObjectName(_fromUtf8("menuInstituciones"))
        self.menuEducativas = QtGui.QMenu(self.menuInstituciones)
        self.menuEducativas.setEnabled(True)
        self.menuEducativas.setObjectName(_fromUtf8("menuEducativas"))
        self.menuDonador = QtGui.QMenu(self.menuInstituciones)
        self.menuDonador.setEnabled(True)
        self.menuDonador.setObjectName(_fromUtf8("menuDonador"))
        self.menuAgregarDonador = QtGui.QMenu(self.menuDonador)
        self.menuAgregarDonador.setEnabled(True)
        self.menuAgregarDonador.setObjectName(_fromUtf8("menuAgregarDonador"))
        self.menuAreas = QtGui.QMenu(self.menuBar)
        self.menuAreas.setObjectName(_fromUtf8("menuAreas"))
        self.menuReportes = QtGui.QMenu(self.menuBar)
        self.menuReportes.setObjectName(_fromUtf8("menuReportes"))
        self.menuGenerar = QtGui.QMenu(self.menuReportes)
        self.menuGenerar.setObjectName(_fromUtf8("menuGenerar"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionAgregarEmpleado = QtGui.QAction(MainWindow)
        self.actionAgregarEmpleado.setEnabled(True)
        self.actionAgregarEmpleado.setVisible(True)
        self.actionAgregarEmpleado.setObjectName(_fromUtf8("actionAgregarEmpleado"))
        self.actionAgregarVoluntario = QtGui.QAction(MainWindow)
        self.actionAgregarVoluntario.setObjectName(_fromUtf8("actionAgregarVoluntario"))
        self.actionAgregarAlumno = QtGui.QAction(MainWindow)
        self.actionAgregarAlumno.setObjectName(_fromUtf8("actionAgregarAlumno"))
        self.actionVerEmpleado = QtGui.QAction(MainWindow)
        self.actionVerEmpleado.setObjectName(_fromUtf8("actionVerEmpleado"))
        self.actionVerNino = QtGui.QAction(MainWindow)
        self.actionVerNino.setObjectName(_fromUtf8("actionVerNino"))
        self.actionVerAdulto = QtGui.QAction(MainWindow)
        self.actionVerAdulto.setObjectName(_fromUtf8("actionVerAdulto"))
        self.actionEmpleado_3 = QtGui.QAction(MainWindow)
        self.actionEmpleado_3.setObjectName(_fromUtf8("actionEmpleado_3"))
        self.actionAgregarCurso = QtGui.QAction(MainWindow)
        self.actionAgregarCurso.setObjectName(_fromUtf8("actionAgregarCurso"))
        self.actionVerCurso = QtGui.QAction(MainWindow)
        self.actionVerCurso.setObjectName(_fromUtf8("actionVerCurso"))
        self.actionDonador = QtGui.QAction(MainWindow)
        self.actionDonador.setObjectName(_fromUtf8("actionDonador"))
        self.actionDonador_2 = QtGui.QAction(MainWindow)
        self.actionDonador_2.setObjectName(_fromUtf8("actionDonador_2"))
        self.actionVer_3 = QtGui.QAction(MainWindow)
        self.actionVer_3.setObjectName(_fromUtf8("actionVer_3"))
        self.actionAgregarArea = QtGui.QAction(MainWindow)
        self.actionAgregarArea.setObjectName(_fromUtf8("actionAgregarArea"))
        self.actionVerArea = QtGui.QAction(MainWindow)
        self.actionVerArea.setObjectName(_fromUtf8("actionVerArea"))
        self.actionAgregarInstitucion = QtGui.QAction(MainWindow)
        self.actionAgregarInstitucion.setObjectName(_fromUtf8("actionAgregarInstitucion"))
        self.actionVerInstitucion = QtGui.QAction(MainWindow)
        self.actionVerInstitucion.setObjectName(_fromUtf8("actionVerInstitucion"))
        self.actionDonador_3 = QtGui.QAction(MainWindow)
        self.actionDonador_3.setObjectName(_fromUtf8("actionDonador_3"))
        self.actionVerDonador = QtGui.QAction(MainWindow)
        self.actionVerDonador.setObjectName(_fromUtf8("actionVerDonador"))
        self.actionAgregarDonador = QtGui.QAction(MainWindow)
        self.actionAgregarDonador.setObjectName(_fromUtf8("actionAgregarDonador"))
        self.actionAgregarClasificacion = QtGui.QAction(MainWindow)
        self.actionAgregarClasificacion.setObjectName(_fromUtf8("actionAgregarClasificacion"))
        self.actionVerVoluntario = QtGui.QAction(MainWindow)
        self.actionVerVoluntario.setObjectName(_fromUtf8("actionVerVoluntario"))
        self.actionVia_Donacion = QtGui.QAction(MainWindow)
        self.actionVia_Donacion.setObjectName(_fromUtf8("actionVia_Donacion"))
        self.actionAgregarPrestador_de_Servicio = QtGui.QAction(MainWindow)
        self.actionAgregarPrestador_de_Servicio.setObjectName(_fromUtf8("actionAgregarPrestador_de_Servicio"))
        self.actionAgregarPracticante = QtGui.QAction(MainWindow)
        self.actionAgregarPracticante.setObjectName(_fromUtf8("actionAgregarPracticante"))
        self.actionVerPrestador_de_Servicio = QtGui.QAction(MainWindow)
        self.actionVerPrestador_de_Servicio.setObjectName(_fromUtf8("actionVerPrestador_de_Servicio"))
        self.actionVerPracticante = QtGui.QAction(MainWindow)
        self.actionVerPracticante.setObjectName(_fromUtf8("actionVerPracticante"))
        self.actionExcell = QtGui.QAction(MainWindow)
        self.actionExcell.setObjectName(_fromUtf8("actionExcell"))
        self.menuEstudiante.addSeparator()
        self.menuEstudiante.addAction(self.actionAgregarPrestador_de_Servicio)
        self.menuEstudiante.addAction(self.actionAgregarPracticante)
        self.menuAgregar.addAction(self.actionAgregarEmpleado)
        self.menuAgregar.addAction(self.actionAgregarVoluntario)
        self.menuAgregar.addAction(self.actionAgregarAlumno)
        self.menuAgregar.addAction(self.menuEstudiante.menuAction())
        self.menuEstudiante_2.addAction(self.actionVerPrestador_de_Servicio)
        self.menuEstudiante_2.addAction(self.actionVerPracticante)
        self.menuVer.addAction(self.actionVerEmpleado)
        self.menuVer.addAction(self.menuEstudiante_2.menuAction())
        self.menuVer.addAction(self.actionVerNino)
        self.menuVer.addAction(self.actionVerAdulto)
        self.menuVer.addAction(self.actionVerVoluntario)
        self.menuUsuario.addAction(self.menuAgregar.menuAction())
        self.menuUsuario.addAction(self.menuVer.menuAction())
        self.menuCursos.addAction(self.actionVerCurso)
        self.menuEducativas.addAction(self.actionAgregarInstitucion)
        self.menuEducativas.addAction(self.actionVerInstitucion)
        self.menuAgregarDonador.addAction(self.actionAgregarDonador)
        self.menuAgregarDonador.addAction(self.actionAgregarClasificacion)
        self.menuAgregarDonador.addAction(self.actionVia_Donacion)
        self.menuDonador.addAction(self.menuAgregarDonador.menuAction())
        self.menuDonador.addAction(self.actionVerDonador)
        self.menuInstituciones.addAction(self.menuEducativas.menuAction())
        self.menuInstituciones.addAction(self.menuDonador.menuAction())
        self.menuAreas.addAction(self.actionAgregarArea)
        self.menuAreas.addAction(self.actionVerArea)
        self.menuGenerar.addAction(self.actionExcell)
        self.menuReportes.addAction(self.menuGenerar.menuAction())
        self.menuBar.addAction(self.menuUsuario.menuAction())
        self.menuBar.addAction(self.menuCursos.menuAction())
        self.menuBar.addAction(self.menuInstituciones.menuAction())
        self.menuBar.addAction(self.menuAreas.menuAction())
        self.menuBar.addAction(self.menuReportes.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionAgregarEmpleado, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.agregarEmpleado)
        QtCore.QObject.connect(self.actionAgregarVoluntario, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.agregarVoluntario)
        QtCore.QObject.connect(self.actionAgregarAlumno, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.agregarAlumno)
        QtCore.QObject.connect(self.actionVerEmpleado, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.verEmpleado)
        QtCore.QObject.connect(self.actionVerNino, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.verNino)
        QtCore.QObject.connect(self.actionVerAdulto, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.verAdulto)
        QtCore.QObject.connect(self.actionVerCurso, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.verCurso)
        QtCore.QObject.connect(self.actionAgregarInstitucion, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.agregarInstitucion)
        QtCore.QObject.connect(self.actionVerInstitucion, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.verInstitucion)
        QtCore.QObject.connect(self.actionAgregarDonador, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.agregarDonador)
        QtCore.QObject.connect(self.actionAgregarClasificacion, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.agregarClasificacion)
        QtCore.QObject.connect(self.actionVerDonador, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.verDonador)
        QtCore.QObject.connect(self.actionAgregarArea, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.agregarArea)
        QtCore.QObject.connect(self.actionVerArea, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.verArea)
        QtCore.QObject.connect(self.actionVerVoluntario, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.verVoluntario)
        QtCore.QObject.connect(self.actionVia_Donacion, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.agregarViaDonacion)
        QtCore.QObject.connect(self.ActualizarBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.actualizar)
        QtCore.QObject.connect(self.actionAgregarPracticante, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.agregarPracticante)
        QtCore.QObject.connect(self.actionAgregarPrestador_de_Servicio, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.agregarPrestador)
        QtCore.QObject.connect(self.actionVerPracticante, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.verPracticante)
        QtCore.QObject.connect(self.actionVerPrestador_de_Servicio, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.verPrestador)
        QtCore.QObject.connect(self.filtroTxt, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), MainWindow.actualizarFiltro)
        QtCore.QObject.connect(self.tipoFiltroComboBox, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), MainWindow.actualizarFiltro)
        QtCore.QObject.connect(self.tableWidgetInfo, QtCore.SIGNAL(_fromUtf8("doubleClicked(QModelIndex)")), MainWindow.agregarFilaAActualizar)
        QtCore.QObject.connect(self.copiarBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.copiar)
        QtCore.QObject.connect(self.actionExcell, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.enviarExcell)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Sistema Informacion Crece", None))
        self.filtroLbl.setText(_translate("MainWindow", "Filtro:", None))
        self.ActualizarBtn.setText(_translate("MainWindow", "Actualizar", None))
        self.copiarBtn.setText(_translate("MainWindow", "Copiar", None))
        self.menuUsuario.setTitle(_translate("MainWindow", "Persona", None))
        self.menuAgregar.setTitle(_translate("MainWindow", "Agregar", None))
        self.menuEstudiante.setTitle(_translate("MainWindow", "Estudiante", None))
        self.menuVer.setTitle(_translate("MainWindow", "Ver", None))
        self.menuEstudiante_2.setTitle(_translate("MainWindow", "Estudiante", None))
        self.menuCursos.setTitle(_translate("MainWindow", "Programas", None))
        self.menuInstituciones.setTitle(_translate("MainWindow", "Instituciones", None))
        self.menuEducativas.setTitle(_translate("MainWindow", "Educativas", None))
        self.menuDonador.setTitle(_translate("MainWindow", "Donador", None))
        self.menuAgregarDonador.setTitle(_translate("MainWindow", "Agregar", None))
        self.menuAreas.setTitle(_translate("MainWindow", "Áreas", None))
        self.menuReportes.setTitle(_translate("MainWindow", "Reportes", None))
        self.menuGenerar.setTitle(_translate("MainWindow", "Generar", None))
        self.actionAgregarEmpleado.setText(_translate("MainWindow", "Empleado", None))
        self.actionAgregarVoluntario.setText(_translate("MainWindow", "Voluntario", None))
        self.actionAgregarAlumno.setText(_translate("MainWindow", "Alumno", None))
        self.actionVerEmpleado.setText(_translate("MainWindow", "Empleado", None))
        self.actionVerNino.setText(_translate("MainWindow", "Niño", None))
        self.actionVerAdulto.setText(_translate("MainWindow", "Adulto", None))
        self.actionEmpleado_3.setText(_translate("MainWindow", "Empleado", None))
        self.actionAgregarCurso.setText(_translate("MainWindow", "Agregar", None))
        self.actionVerCurso.setText(_translate("MainWindow", "Ver", None))
        self.actionDonador.setText(_translate("MainWindow", "Donador", None))
        self.actionDonador_2.setText(_translate("MainWindow", "Donador", None))
        self.actionVer_3.setText(_translate("MainWindow", "Ver", None))
        self.actionAgregarArea.setText(_translate("MainWindow", "Agregar", None))
        self.actionVerArea.setText(_translate("MainWindow", "Ver", None))
        self.actionAgregarInstitucion.setText(_translate("MainWindow", "Agregar", None))
        self.actionVerInstitucion.setText(_translate("MainWindow", "Ver", None))
        self.actionDonador_3.setText(_translate("MainWindow", "Donador", None))
        self.actionVerDonador.setText(_translate("MainWindow", "Ver", None))
        self.actionAgregarDonador.setText(_translate("MainWindow", "Donador", None))
        self.actionAgregarClasificacion.setText(_translate("MainWindow", "Clasificacion", None))
        self.actionVerVoluntario.setText(_translate("MainWindow", "Voluntario", None))
        self.actionVia_Donacion.setText(_translate("MainWindow", "Vía Donación", None))
        self.actionAgregarPrestador_de_Servicio.setText(_translate("MainWindow", "Prestador de Servicio", None))
        self.actionAgregarPracticante.setText(_translate("MainWindow", "Practicante", None))
        self.actionVerPrestador_de_Servicio.setText(_translate("MainWindow", "Prestador de Servicio", None))
        self.actionVerPracticante.setText(_translate("MainWindow", "Practicante", None))
        self.actionExcell.setText(_translate("MainWindow", "Excel", None))

