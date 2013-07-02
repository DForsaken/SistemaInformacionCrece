/********************************************************************************
** Form generated from reading UI file 'Principal.ui'
**
** Created: Mon 17. Jun 23:12:26 2013
**      by: Qt User Interface Compiler version 4.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_PRINCIPAL_H
#define UI_PRINCIPAL_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QDockWidget>
#include <QtGui/QHeaderView>
#include <QtGui/QMainWindow>
#include <QtGui/QMenu>
#include <QtGui/QMenuBar>
#include <QtGui/QStatusBar>
#include <QtGui/QTableWidget>
#include <QtGui/QToolBar>
#include <QtGui/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionAgregarEmpleado;
    QAction *actionAgregarNino;
    QAction *actionAgregarAdulto;
    QAction *actionAgregarEstudiante;
    QAction *actionVerEmpleado;
    QAction *actionVerEstudiante;
    QAction *actionVerNino;
    QAction *actionVerAdulto;
    QAction *actionEmpleado_3;
    QAction *actionAgregarCurso;
    QAction *actionVerCurso;
    QAction *actionDonador;
    QAction *actionDonador_2;
    QAction *actionVer_3;
    QAction *actionAgregarArea;
    QAction *actionVerArea;
    QAction *actionAgregarInstitucion;
    QAction *actionVerInstitucion;
    QAction *actionDonador_3;
    QAction *actionVerDonador;
    QAction *actionAgregarDonador;
    QAction *actionAgregarClasificacion;
    QWidget *centralWidget;
    QDockWidget *dockWidgetInfo;
    QWidget *dockWidgetContents_3;
    QTableWidget *tableWidgetInfo;
    QMenuBar *menuBar;
    QMenu *menuUsuario;
    QMenu *menuAgregar;
    QMenu *menuVer;
    QMenu *menuCursos;
    QMenu *menuInstituciones;
    QMenu *menuEducativas;
    QMenu *menuDonador;
    QMenu *menuAgregar_2;
    QMenu *menuAreas;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(400, 300);
        actionAgregarEmpleado = new QAction(MainWindow);
        actionAgregarEmpleado->setObjectName(QString::fromUtf8("actionAgregarEmpleado"));
        actionAgregarNino = new QAction(MainWindow);
        actionAgregarNino->setObjectName(QString::fromUtf8("actionAgregarNino"));
        actionAgregarAdulto = new QAction(MainWindow);
        actionAgregarAdulto->setObjectName(QString::fromUtf8("actionAgregarAdulto"));
        actionAgregarEstudiante = new QAction(MainWindow);
        actionAgregarEstudiante->setObjectName(QString::fromUtf8("actionAgregarEstudiante"));
        actionVerEmpleado = new QAction(MainWindow);
        actionVerEmpleado->setObjectName(QString::fromUtf8("actionVerEmpleado"));
        actionVerEstudiante = new QAction(MainWindow);
        actionVerEstudiante->setObjectName(QString::fromUtf8("actionVerEstudiante"));
        actionVerNino = new QAction(MainWindow);
        actionVerNino->setObjectName(QString::fromUtf8("actionVerNino"));
        actionVerAdulto = new QAction(MainWindow);
        actionVerAdulto->setObjectName(QString::fromUtf8("actionVerAdulto"));
        actionEmpleado_3 = new QAction(MainWindow);
        actionEmpleado_3->setObjectName(QString::fromUtf8("actionEmpleado_3"));
        actionAgregarCurso = new QAction(MainWindow);
        actionAgregarCurso->setObjectName(QString::fromUtf8("actionAgregarCurso"));
        actionVerCurso = new QAction(MainWindow);
        actionVerCurso->setObjectName(QString::fromUtf8("actionVerCurso"));
        actionDonador = new QAction(MainWindow);
        actionDonador->setObjectName(QString::fromUtf8("actionDonador"));
        actionDonador_2 = new QAction(MainWindow);
        actionDonador_2->setObjectName(QString::fromUtf8("actionDonador_2"));
        actionVer_3 = new QAction(MainWindow);
        actionVer_3->setObjectName(QString::fromUtf8("actionVer_3"));
        actionAgregarArea = new QAction(MainWindow);
        actionAgregarArea->setObjectName(QString::fromUtf8("actionAgregarArea"));
        actionVerArea = new QAction(MainWindow);
        actionVerArea->setObjectName(QString::fromUtf8("actionVerArea"));
        actionAgregarInstitucion = new QAction(MainWindow);
        actionAgregarInstitucion->setObjectName(QString::fromUtf8("actionAgregarInstitucion"));
        actionVerInstitucion = new QAction(MainWindow);
        actionVerInstitucion->setObjectName(QString::fromUtf8("actionVerInstitucion"));
        actionDonador_3 = new QAction(MainWindow);
        actionDonador_3->setObjectName(QString::fromUtf8("actionDonador_3"));
        actionVerDonador = new QAction(MainWindow);
        actionVerDonador->setObjectName(QString::fromUtf8("actionVerDonador"));
        actionAgregarDonador = new QAction(MainWindow);
        actionAgregarDonador->setObjectName(QString::fromUtf8("actionAgregarDonador"));
        actionAgregarClasificacion = new QAction(MainWindow);
        actionAgregarClasificacion->setObjectName(QString::fromUtf8("actionAgregarClasificacion"));
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        dockWidgetInfo = new QDockWidget(centralWidget);
        dockWidgetInfo->setObjectName(QString::fromUtf8("dockWidgetInfo"));
        dockWidgetInfo->setGeometry(QRect(10, 0, 347, 247));
        dockWidgetInfo->setAutoFillBackground(true);
        dockWidgetInfo->setFloating(false);
        dockWidgetInfo->setFeatures(QDockWidget::DockWidgetClosable);
        dockWidgetInfo->setAllowedAreas(Qt::AllDockWidgetAreas);
        dockWidgetContents_3 = new QWidget();
        dockWidgetContents_3->setObjectName(QString::fromUtf8("dockWidgetContents_3"));
        tableWidgetInfo = new QTableWidget(dockWidgetContents_3);
        tableWidgetInfo->setObjectName(QString::fromUtf8("tableWidgetInfo"));
        tableWidgetInfo->setGeometry(QRect(10, 10, 331, 171));
        dockWidgetInfo->setWidget(dockWidgetContents_3);
        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 400, 21));
        menuUsuario = new QMenu(menuBar);
        menuUsuario->setObjectName(QString::fromUtf8("menuUsuario"));
        menuAgregar = new QMenu(menuUsuario);
        menuAgregar->setObjectName(QString::fromUtf8("menuAgregar"));
        menuVer = new QMenu(menuUsuario);
        menuVer->setObjectName(QString::fromUtf8("menuVer"));
        menuCursos = new QMenu(menuBar);
        menuCursos->setObjectName(QString::fromUtf8("menuCursos"));
        menuInstituciones = new QMenu(menuBar);
        menuInstituciones->setObjectName(QString::fromUtf8("menuInstituciones"));
        menuEducativas = new QMenu(menuInstituciones);
        menuEducativas->setObjectName(QString::fromUtf8("menuEducativas"));
        menuDonador = new QMenu(menuInstituciones);
        menuDonador->setObjectName(QString::fromUtf8("menuDonador"));
        menuAgregar_2 = new QMenu(menuDonador);
        menuAgregar_2->setObjectName(QString::fromUtf8("menuAgregar_2"));
        menuAreas = new QMenu(menuBar);
        menuAreas->setObjectName(QString::fromUtf8("menuAreas"));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        MainWindow->setStatusBar(statusBar);

        menuBar->addAction(menuUsuario->menuAction());
        menuBar->addAction(menuCursos->menuAction());
        menuBar->addAction(menuInstituciones->menuAction());
        menuBar->addAction(menuAreas->menuAction());
        menuUsuario->addAction(menuAgregar->menuAction());
        menuUsuario->addAction(menuVer->menuAction());
        menuAgregar->addAction(actionAgregarEmpleado);
        menuAgregar->addAction(actionAgregarNino);
        menuAgregar->addAction(actionAgregarAdulto);
        menuAgregar->addAction(actionAgregarEstudiante);
        menuVer->addAction(actionVerEmpleado);
        menuVer->addAction(actionVerEstudiante);
        menuVer->addAction(actionVerNino);
        menuVer->addAction(actionVerAdulto);
        menuCursos->addAction(actionVerCurso);
        menuInstituciones->addAction(menuEducativas->menuAction());
        menuInstituciones->addAction(menuDonador->menuAction());
        menuEducativas->addAction(actionAgregarInstitucion);
        menuEducativas->addAction(actionVerInstitucion);
        menuDonador->addAction(menuAgregar_2->menuAction());
        menuDonador->addAction(actionVerDonador);
        menuAgregar_2->addAction(actionAgregarDonador);
        menuAgregar_2->addAction(actionAgregarClasificacion);
        menuAreas->addAction(actionAgregarArea);
        menuAreas->addAction(actionVerArea);

        retranslateUi(MainWindow);
        QObject::connect(actionAgregarEmpleado, SIGNAL(triggered()), MainWindow, SLOT(agregarEmpleado()));
        QObject::connect(actionAgregarNino, SIGNAL(triggered()), MainWindow, SLOT(agregarNino()));
        QObject::connect(actionAgregarAdulto, SIGNAL(triggered()), MainWindow, SLOT(agregarAdulto()));
        QObject::connect(actionAgregarEstudiante, SIGNAL(triggered()), MainWindow, SLOT(agregarEstudiante()));
        QObject::connect(actionVerEmpleado, SIGNAL(triggered()), MainWindow, SLOT(verEmpleado()));
        QObject::connect(actionVerEstudiante, SIGNAL(triggered()), MainWindow, SLOT(verEstudiante()));
        QObject::connect(actionVerNino, SIGNAL(triggered()), MainWindow, SLOT(verNino()));
        QObject::connect(actionVerAdulto, SIGNAL(triggered()), MainWindow, SLOT(verAdulto()));
        QObject::connect(actionVerCurso, SIGNAL(triggered()), MainWindow, SLOT(verCurso()));
        QObject::connect(actionAgregarInstitucion, SIGNAL(triggered()), MainWindow, SLOT(agregarInstitucion()));
        QObject::connect(actionVerInstitucion, SIGNAL(triggered()), MainWindow, SLOT(verInstitucion()));
        QObject::connect(actionAgregarDonador, SIGNAL(triggered()), MainWindow, SLOT(agregarDonador()));
        QObject::connect(actionAgregarClasificacion, SIGNAL(triggered()), MainWindow, SLOT(agregarClasificacion()));
        QObject::connect(actionVerDonador, SIGNAL(triggered()), MainWindow, SLOT(verDonador()));
        QObject::connect(actionAgregarArea, SIGNAL(triggered()), MainWindow, SLOT(agregarArea()));
        QObject::connect(actionVerArea, SIGNAL(triggered()), MainWindow, SLOT(verArea()));

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", 0, QApplication::UnicodeUTF8));
        actionAgregarEmpleado->setText(QApplication::translate("MainWindow", "Empleado", 0, QApplication::UnicodeUTF8));
        actionAgregarNino->setText(QApplication::translate("MainWindow", "Ni\303\261o", 0, QApplication::UnicodeUTF8));
        actionAgregarAdulto->setText(QApplication::translate("MainWindow", "Adulto", 0, QApplication::UnicodeUTF8));
        actionAgregarEstudiante->setText(QApplication::translate("MainWindow", "Estudiante", 0, QApplication::UnicodeUTF8));
        actionVerEmpleado->setText(QApplication::translate("MainWindow", "Empleado", 0, QApplication::UnicodeUTF8));
        actionVerEstudiante->setText(QApplication::translate("MainWindow", "Estudiante", 0, QApplication::UnicodeUTF8));
        actionVerNino->setText(QApplication::translate("MainWindow", "Ni\303\261o", 0, QApplication::UnicodeUTF8));
        actionVerAdulto->setText(QApplication::translate("MainWindow", "Adulto", 0, QApplication::UnicodeUTF8));
        actionEmpleado_3->setText(QApplication::translate("MainWindow", "Empleado", 0, QApplication::UnicodeUTF8));
        actionAgregarCurso->setText(QApplication::translate("MainWindow", "Agregar", 0, QApplication::UnicodeUTF8));
        actionVerCurso->setText(QApplication::translate("MainWindow", "Ver", 0, QApplication::UnicodeUTF8));
        actionDonador->setText(QApplication::translate("MainWindow", "Donador", 0, QApplication::UnicodeUTF8));
        actionDonador_2->setText(QApplication::translate("MainWindow", "Donador", 0, QApplication::UnicodeUTF8));
        actionVer_3->setText(QApplication::translate("MainWindow", "Ver", 0, QApplication::UnicodeUTF8));
        actionAgregarArea->setText(QApplication::translate("MainWindow", "Agregar", 0, QApplication::UnicodeUTF8));
        actionVerArea->setText(QApplication::translate("MainWindow", "Ver", 0, QApplication::UnicodeUTF8));
        actionAgregarInstitucion->setText(QApplication::translate("MainWindow", "Agregar", 0, QApplication::UnicodeUTF8));
        actionVerInstitucion->setText(QApplication::translate("MainWindow", "Ver", 0, QApplication::UnicodeUTF8));
        actionDonador_3->setText(QApplication::translate("MainWindow", "Donador", 0, QApplication::UnicodeUTF8));
        actionVerDonador->setText(QApplication::translate("MainWindow", "Ver", 0, QApplication::UnicodeUTF8));
        actionAgregarDonador->setText(QApplication::translate("MainWindow", "Donador", 0, QApplication::UnicodeUTF8));
        actionAgregarClasificacion->setText(QApplication::translate("MainWindow", "Clasificacion", 0, QApplication::UnicodeUTF8));
        menuUsuario->setTitle(QApplication::translate("MainWindow", "Persona", 0, QApplication::UnicodeUTF8));
        menuAgregar->setTitle(QApplication::translate("MainWindow", "Agregar", 0, QApplication::UnicodeUTF8));
        menuVer->setTitle(QApplication::translate("MainWindow", "Ver", 0, QApplication::UnicodeUTF8));
        menuCursos->setTitle(QApplication::translate("MainWindow", "Cursos", 0, QApplication::UnicodeUTF8));
        menuInstituciones->setTitle(QApplication::translate("MainWindow", "Instituciones", 0, QApplication::UnicodeUTF8));
        menuEducativas->setTitle(QApplication::translate("MainWindow", "Educativas", 0, QApplication::UnicodeUTF8));
        menuDonador->setTitle(QApplication::translate("MainWindow", "Donador", 0, QApplication::UnicodeUTF8));
        menuAgregar_2->setTitle(QApplication::translate("MainWindow", "Agregar", 0, QApplication::UnicodeUTF8));
        menuAreas->setTitle(QApplication::translate("MainWindow", "\303\201reas", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_PRINCIPAL_H
