# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Principal.ui'
#
# Created: Sun Oct 27 21:33:09 2013
#      by: PyQt4 UI code generator 4.10
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
        MainWindow.resize(400, 300)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.dockWidgetInfo = QtGui.QDockWidget(self.centralWidget)
        self.dockWidgetInfo.setGeometry(QtCore.QRect(10, 0, 347, 247))
        self.dockWidgetInfo.setAutoFillBackground(True)
        self.dockWidgetInfo.setFloating(False)
        self.dockWidgetInfo.setFeatures(QtGui.QDockWidget.DockWidgetClosable)
        self.dockWidgetInfo.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.dockWidgetInfo.setObjectName(_fromUtf8("dockWidgetInfo"))
        self.dockWidgetContents_3 = QtGui.QWidget()
        self.dockWidgetContents_3.setObjectName(_fromUtf8("dockWidgetContents_3"))
        self.tableWidgetInfo = QtGui.QTableWidget(self.dockWidgetContents_3)
        self.tableWidgetInfo.setGeometry(QtCore.QRect(10, 10, 331, 171))
        self.tableWidgetInfo.setObjectName(_fromUtf8("tableWidgetInfo"))
        self.tableWidgetInfo.setColumnCount(0)
        self.tableWidgetInfo.setRowCount(0)
        self.dockWidgetInfo.setWidget(self.dockWidgetContents_3)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuUsuario = QtGui.QMenu(self.menuBar)
        self.menuUsuario.setObjectName(_fromUtf8("menuUsuario"))
        self.menuAgregar = QtGui.QMenu(self.menuUsuario)
        self.menuAgregar.setObjectName(_fromUtf8("menuAgregar"))
        self.menuVer = QtGui.QMenu(self.menuUsuario)
        self.menuVer.setObjectName(_fromUtf8("menuVer"))
        self.menuCursos = QtGui.QMenu(self.menuBar)
        self.menuCursos.setObjectName(_fromUtf8("menuCursos"))
        self.menuInstituciones = QtGui.QMenu(self.menuBar)
        self.menuInstituciones.setObjectName(_fromUtf8("menuInstituciones"))
        self.menuEducativas = QtGui.QMenu(self.menuInstituciones)
        self.menuEducativas.setObjectName(_fromUtf8("menuEducativas"))
        self.menuDonador = QtGui.QMenu(self.menuInstituciones)
        self.menuDonador.setObjectName(_fromUtf8("menuDonador"))
        self.menuAgregar_2 = QtGui.QMenu(self.menuDonador)
        self.menuAgregar_2.setObjectName(_fromUtf8("menuAgregar_2"))
        self.menuAreas = QtGui.QMenu(self.menuBar)
        self.menuAreas.setObjectName(_fromUtf8("menuAreas"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionAgregarEmpleado = QtGui.QAction(MainWindow)
        self.actionAgregarEmpleado.setObjectName(_fromUtf8("actionAgregarEmpleado"))
        self.actionAgregarNino = QtGui.QAction(MainWindow)
        self.actionAgregarNino.setObjectName(_fromUtf8("actionAgregarNino"))
        self.actionAgregarAdulto = QtGui.QAction(MainWindow)
        self.actionAgregarAdulto.setObjectName(_fromUtf8("actionAgregarAdulto"))
        self.actionAgregarEstudiante = QtGui.QAction(MainWindow)
        self.actionAgregarEstudiante.setObjectName(_fromUtf8("actionAgregarEstudiante"))
        self.actionVerEmpleado = QtGui.QAction(MainWindow)
        self.actionVerEmpleado.setObjectName(_fromUtf8("actionVerEmpleado"))
        self.actionVerEstudiante = QtGui.QAction(MainWindow)
        self.actionVerEstudiante.setObjectName(_fromUtf8("actionVerEstudiante"))
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
        self.menuAgregar.addAction(self.actionAgregarEmpleado)
        self.menuAgregar.addAction(self.actionAgregarNino)
        self.menuAgregar.addAction(self.actionAgregarAdulto)
        self.menuAgregar.addAction(self.actionAgregarEstudiante)
        self.menuVer.addAction(self.actionVerEmpleado)
        self.menuVer.addAction(self.actionVerEstudiante)
        self.menuVer.addAction(self.actionVerNino)
        self.menuVer.addAction(self.actionVerAdulto)
        self.menuUsuario.addAction(self.menuAgregar.menuAction())
        self.menuUsuario.addAction(self.menuVer.menuAction())
        self.menuCursos.addAction(self.actionVerCurso)
        self.menuEducativas.addAction(self.actionAgregarInstitucion)
        self.menuEducativas.addAction(self.actionVerInstitucion)
        self.menuAgregar_2.addAction(self.actionAgregarDonador)
        self.menuAgregar_2.addAction(self.actionAgregarClasificacion)
        self.menuDonador.addAction(self.menuAgregar_2.menuAction())
        self.menuDonador.addAction(self.actionVerDonador)
        self.menuInstituciones.addAction(self.menuEducativas.menuAction())
        self.menuInstituciones.addAction(self.menuDonador.menuAction())
        self.menuAreas.addAction(self.actionAgregarArea)
        self.menuAreas.addAction(self.actionVerArea)
        self.menuBar.addAction(self.menuUsuario.menuAction())
        self.menuBar.addAction(self.menuCursos.menuAction())
        self.menuBar.addAction(self.menuInstituciones.menuAction())
        self.menuBar.addAction(self.menuAreas.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionAgregarEmpleado, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.agregarEmpleado)
        QtCore.QObject.connect(self.actionAgregarNino, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.agregarNino)
        QtCore.QObject.connect(self.actionAgregarAdulto, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.agregarAdulto)
        QtCore.QObject.connect(self.actionAgregarEstudiante, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.agregarEstudiante)
        QtCore.QObject.connect(self.actionVerEmpleado, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.verEmpleado)
        QtCore.QObject.connect(self.actionVerEstudiante, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.verEstudiante)
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
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menuUsuario.setTitle(_translate("MainWindow", "Persona", None))
        self.menuAgregar.setTitle(_translate("MainWindow", "Agregar", None))
        self.menuVer.setTitle(_translate("MainWindow", "Ver", None))
        self.menuCursos.setTitle(_translate("MainWindow", "Cursos", None))
        self.menuInstituciones.setTitle(_translate("MainWindow", "Instituciones", None))
        self.menuEducativas.setTitle(_translate("MainWindow", "Educativas", None))
        self.menuDonador.setTitle(_translate("MainWindow", "Donador", None))
        self.menuAgregar_2.setTitle(_translate("MainWindow", "Agregar", None))
        self.menuAreas.setTitle(_translate("MainWindow", "Áreas", None))
        self.actionAgregarEmpleado.setText(_translate("MainWindow", "Empleado", None))
        self.actionAgregarNino.setText(_translate("MainWindow", "Niño", None))
        self.actionAgregarAdulto.setText(_translate("MainWindow", "Adulto", None))
        self.actionAgregarEstudiante.setText(_translate("MainWindow", "Estudiante", None))
        self.actionVerEmpleado.setText(_translate("MainWindow", "Empleado", None))
        self.actionVerEstudiante.setText(_translate("MainWindow", "Estudiante", None))
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

