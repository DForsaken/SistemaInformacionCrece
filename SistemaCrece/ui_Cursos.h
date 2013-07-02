/********************************************************************************
** Form generated from reading UI file 'Cursos.ui'
**
** Created: Mon 17. Jun 23:12:27 2013
**      by: Qt User Interface Compiler version 4.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_CURSOS_H
#define UI_CURSOS_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QComboBox>
#include <QtGui/QDockWidget>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QLineEdit>
#include <QtGui/QMainWindow>
#include <QtGui/QMenu>
#include <QtGui/QMenuBar>
#include <QtGui/QStatusBar>
#include <QtGui/QTableWidget>
#include <QtGui/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionVerLista_cursos;
    QAction *actionVerAlumnos;
    QAction *actionAlumno;
    QAction *actionCurso;
    QAction *actionTemporada;
    QAction *actionAgregaCurso;
    QAction *actionAgregarMaestro;
    QAction *actionAgregarEstudiante;
    QAction *actionVerMaestros;
    QAction *actionVerEstudiantes;
    QAction *actionVerAlumno;
    QAction *actionAyudante_2;
    QAction *actionVerLista_asistencia;
    QAction *actionCausa_falta;
    QAction *actionNuevo;
    QAction *actionNuevoAlumno;
    QAction *actionExistente;
    QWidget *centralwidget;
    QDockWidget *dockWidget;
    QWidget *dockWidgetContents;
    QLabel *busquedaLbl;
    QComboBox *FiltroComboBox;
    QLineEdit *busquedaTxt;
    QLabel *filtroLbl;
    QTableWidget *infoTableWidget;
    QMenuBar *menubar;
    QMenu *menuCursos;
    QMenu *menuVer;
    QMenu *menuAgregar;
    QMenu *menuAlumnos;
    QMenu *menuAgregarAlumno;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(465, 361);
        actionVerLista_cursos = new QAction(MainWindow);
        actionVerLista_cursos->setObjectName(QString::fromUtf8("actionVerLista_cursos"));
        actionVerAlumnos = new QAction(MainWindow);
        actionVerAlumnos->setObjectName(QString::fromUtf8("actionVerAlumnos"));
        actionAlumno = new QAction(MainWindow);
        actionAlumno->setObjectName(QString::fromUtf8("actionAlumno"));
        actionCurso = new QAction(MainWindow);
        actionCurso->setObjectName(QString::fromUtf8("actionCurso"));
        actionTemporada = new QAction(MainWindow);
        actionTemporada->setObjectName(QString::fromUtf8("actionTemporada"));
        actionAgregaCurso = new QAction(MainWindow);
        actionAgregaCurso->setObjectName(QString::fromUtf8("actionAgregaCurso"));
        actionAgregarMaestro = new QAction(MainWindow);
        actionAgregarMaestro->setObjectName(QString::fromUtf8("actionAgregarMaestro"));
        actionAgregarEstudiante = new QAction(MainWindow);
        actionAgregarEstudiante->setObjectName(QString::fromUtf8("actionAgregarEstudiante"));
        actionVerMaestros = new QAction(MainWindow);
        actionVerMaestros->setObjectName(QString::fromUtf8("actionVerMaestros"));
        actionVerEstudiantes = new QAction(MainWindow);
        actionVerEstudiantes->setObjectName(QString::fromUtf8("actionVerEstudiantes"));
        actionVerAlumno = new QAction(MainWindow);
        actionVerAlumno->setObjectName(QString::fromUtf8("actionVerAlumno"));
        actionAyudante_2 = new QAction(MainWindow);
        actionAyudante_2->setObjectName(QString::fromUtf8("actionAyudante_2"));
        actionVerLista_asistencia = new QAction(MainWindow);
        actionVerLista_asistencia->setObjectName(QString::fromUtf8("actionVerLista_asistencia"));
        actionCausa_falta = new QAction(MainWindow);
        actionCausa_falta->setObjectName(QString::fromUtf8("actionCausa_falta"));
        actionNuevo = new QAction(MainWindow);
        actionNuevo->setObjectName(QString::fromUtf8("actionNuevo"));
        actionNuevoAlumno = new QAction(MainWindow);
        actionNuevoAlumno->setObjectName(QString::fromUtf8("actionNuevoAlumno"));
        actionExistente = new QAction(MainWindow);
        actionExistente->setObjectName(QString::fromUtf8("actionExistente"));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        dockWidget = new QDockWidget(centralwidget);
        dockWidget->setObjectName(QString::fromUtf8("dockWidget"));
        dockWidget->setGeometry(QRect(20, 20, 421, 320));
        dockWidget->setFloating(true);
        dockWidget->setFeatures(QDockWidget::DockWidgetClosable|QDockWidget::DockWidgetFloatable);
        dockWidgetContents = new QWidget();
        dockWidgetContents->setObjectName(QString::fromUtf8("dockWidgetContents"));
        busquedaLbl = new QLabel(dockWidgetContents);
        busquedaLbl->setObjectName(QString::fromUtf8("busquedaLbl"));
        busquedaLbl->setGeometry(QRect(10, 10, 61, 16));
        FiltroComboBox = new QComboBox(dockWidgetContents);
        FiltroComboBox->setObjectName(QString::fromUtf8("FiltroComboBox"));
        FiltroComboBox->setGeometry(QRect(70, 40, 111, 22));
        busquedaTxt = new QLineEdit(dockWidgetContents);
        busquedaTxt->setObjectName(QString::fromUtf8("busquedaTxt"));
        busquedaTxt->setGeometry(QRect(70, 10, 113, 20));
        filtroLbl = new QLabel(dockWidgetContents);
        filtroLbl->setObjectName(QString::fromUtf8("filtroLbl"));
        filtroLbl->setGeometry(QRect(10, 40, 46, 13));
        infoTableWidget = new QTableWidget(dockWidgetContents);
        infoTableWidget->setObjectName(QString::fromUtf8("infoTableWidget"));
        infoTableWidget->setGeometry(QRect(10, 70, 401, 192));
        dockWidget->setWidget(dockWidgetContents);
        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 465, 21));
        menuCursos = new QMenu(menubar);
        menuCursos->setObjectName(QString::fromUtf8("menuCursos"));
        menuVer = new QMenu(menuCursos);
        menuVer->setObjectName(QString::fromUtf8("menuVer"));
        menuAgregar = new QMenu(menuCursos);
        menuAgregar->setObjectName(QString::fromUtf8("menuAgregar"));
        menuAlumnos = new QMenu(menubar);
        menuAlumnos->setObjectName(QString::fromUtf8("menuAlumnos"));
        menuAgregarAlumno = new QMenu(menuAlumnos);
        menuAgregarAlumno->setObjectName(QString::fromUtf8("menuAgregarAlumno"));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        MainWindow->setStatusBar(statusbar);

        menubar->addAction(menuCursos->menuAction());
        menubar->addAction(menuAlumnos->menuAction());
        menuCursos->addAction(menuAgregar->menuAction());
        menuCursos->addAction(menuVer->menuAction());
        menuVer->addAction(actionVerLista_cursos);
        menuVer->addAction(actionVerMaestros);
        menuVer->addAction(actionVerEstudiantes);
        menuVer->addAction(actionVerLista_asistencia);
        menuAgregar->addAction(actionAgregaCurso);
        menuAgregar->addAction(actionAgregarMaestro);
        menuAgregar->addAction(actionAgregarEstudiante);
        menuAgregar->addAction(actionCausa_falta);
        menuAlumnos->addAction(menuAgregarAlumno->menuAction());
        menuAlumnos->addAction(actionVerAlumno);
        menuAgregarAlumno->addAction(actionNuevoAlumno);
        menuAgregarAlumno->addAction(actionExistente);

        retranslateUi(MainWindow);
        QObject::connect(actionAgregaCurso, SIGNAL(activated()), MainWindow, SLOT(agregarCurso()));
        QObject::connect(actionAgregarEstudiante, SIGNAL(activated()), MainWindow, SLOT(agregarEstudianteCurso()));
        QObject::connect(actionAgregarMaestro, SIGNAL(activated()), MainWindow, SLOT(agregarMaestroCurso()));
        QObject::connect(actionCausa_falta, SIGNAL(activated()), MainWindow, SLOT(agregarCausaFaltaCurso()));
        QObject::connect(actionVerLista_cursos, SIGNAL(activated()), MainWindow, SLOT(verCatalogoCursos()));
        QObject::connect(actionVerMaestros, SIGNAL(activated()), MainWindow, SLOT(verMaestros()));
        QObject::connect(actionVerEstudiantes, SIGNAL(activated()), MainWindow, SLOT(verEstudiantes()));
        QObject::connect(actionVerLista_asistencia, SIGNAL(activated()), MainWindow, SLOT(verListaAsistencia()));
        QObject::connect(actionNuevoAlumno, SIGNAL(activated()), MainWindow, SLOT(agregarAlumnoCurso()));
        QObject::connect(actionExistente, SIGNAL(activated()), MainWindow, SLOT(agregarAlumnoCurso()));

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", 0, QApplication::UnicodeUTF8));
        actionVerLista_cursos->setText(QApplication::translate("MainWindow", "Catalogo de cursos", 0, QApplication::UnicodeUTF8));
        actionVerAlumnos->setText(QApplication::translate("MainWindow", "Alumnos", 0, QApplication::UnicodeUTF8));
        actionAlumno->setText(QApplication::translate("MainWindow", "Alumno", 0, QApplication::UnicodeUTF8));
        actionCurso->setText(QApplication::translate("MainWindow", "Edad", 0, QApplication::UnicodeUTF8));
        actionTemporada->setText(QApplication::translate("MainWindow", "Maestro", 0, QApplication::UnicodeUTF8));
        actionAgregaCurso->setText(QApplication::translate("MainWindow", "Curso", 0, QApplication::UnicodeUTF8));
        actionAgregarMaestro->setText(QApplication::translate("MainWindow", "Maestro", 0, QApplication::UnicodeUTF8));
        actionAgregarEstudiante->setText(QApplication::translate("MainWindow", "Estudiante", 0, QApplication::UnicodeUTF8));
        actionVerMaestros->setText(QApplication::translate("MainWindow", "Maestros", 0, QApplication::UnicodeUTF8));
        actionVerEstudiantes->setText(QApplication::translate("MainWindow", "Estudiante", 0, QApplication::UnicodeUTF8));
        actionVerAlumno->setText(QApplication::translate("MainWindow", "Ver", 0, QApplication::UnicodeUTF8));
        actionAyudante_2->setText(QApplication::translate("MainWindow", "Estudiante", 0, QApplication::UnicodeUTF8));
        actionVerLista_asistencia->setText(QApplication::translate("MainWindow", "Lista asistencia", 0, QApplication::UnicodeUTF8));
        actionCausa_falta->setText(QApplication::translate("MainWindow", "Causa falta", 0, QApplication::UnicodeUTF8));
        actionNuevo->setText(QApplication::translate("MainWindow", "Nuevo", 0, QApplication::UnicodeUTF8));
        actionNuevoAlumno->setText(QApplication::translate("MainWindow", "Nuevo", 0, QApplication::UnicodeUTF8));
        actionExistente->setText(QApplication::translate("MainWindow", "Existente", 0, QApplication::UnicodeUTF8));
        busquedaLbl->setText(QApplication::translate("MainWindow", "Busqueda:", 0, QApplication::UnicodeUTF8));
        filtroLbl->setText(QApplication::translate("MainWindow", "Filtro:", 0, QApplication::UnicodeUTF8));
        menuCursos->setTitle(QApplication::translate("MainWindow", "Cursos", 0, QApplication::UnicodeUTF8));
        menuVer->setTitle(QApplication::translate("MainWindow", "Ver ", 0, QApplication::UnicodeUTF8));
        menuAgregar->setTitle(QApplication::translate("MainWindow", "Agregar", 0, QApplication::UnicodeUTF8));
        menuAlumnos->setTitle(QApplication::translate("MainWindow", "Alumnos", 0, QApplication::UnicodeUTF8));
        menuAgregarAlumno->setTitle(QApplication::translate("MainWindow", "Agregar", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_CURSOS_H
