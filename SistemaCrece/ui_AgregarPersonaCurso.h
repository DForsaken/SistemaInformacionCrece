/********************************************************************************
** Form generated from reading UI file 'AgregarPersonaCurso.ui'
**
** Created: Mon 17. Jun 23:12:28 2013
**      by: Qt User Interface Compiler version 4.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_AGREGARPERSONACURSO_H
#define UI_AGREGARPERSONACURSO_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QComboBox>
#include <QtGui/QDateEdit>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QPushButton>
#include <QtGui/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Form
{
public:
    QLabel *areaLbl;
    QLabel *nombreLbl;
    QLabel *coloniaLbl;
    QLabel *fechaInicioLbl;
    QLabel *alumnoLbl;
    QComboBox *coloniaComboBox;
    QComboBox *nombreComboBox;
    QComboBox *arecomboBox;
    QComboBox *alumnoComboBox;
    QDateEdit *fechaInicioDate;
    QPushButton *aceptarBtn;
    QPushButton *CancelarBtn;

    void setupUi(QWidget *Form)
    {
        if (Form->objectName().isEmpty())
            Form->setObjectName(QString::fromUtf8("Form"));
        Form->resize(224, 215);
        areaLbl = new QLabel(Form);
        areaLbl->setObjectName(QString::fromUtf8("areaLbl"));
        areaLbl->setGeometry(QRect(20, 20, 46, 13));
        nombreLbl = new QLabel(Form);
        nombreLbl->setObjectName(QString::fromUtf8("nombreLbl"));
        nombreLbl->setGeometry(QRect(20, 50, 46, 13));
        coloniaLbl = new QLabel(Form);
        coloniaLbl->setObjectName(QString::fromUtf8("coloniaLbl"));
        coloniaLbl->setGeometry(QRect(20, 80, 46, 13));
        fechaInicioLbl = new QLabel(Form);
        fechaInicioLbl->setObjectName(QString::fromUtf8("fechaInicioLbl"));
        fechaInicioLbl->setGeometry(QRect(20, 110, 61, 16));
        alumnoLbl = new QLabel(Form);
        alumnoLbl->setObjectName(QString::fromUtf8("alumnoLbl"));
        alumnoLbl->setGeometry(QRect(20, 140, 46, 13));
        coloniaComboBox = new QComboBox(Form);
        coloniaComboBox->setObjectName(QString::fromUtf8("coloniaComboBox"));
        coloniaComboBox->setGeometry(QRect(90, 80, 111, 21));
        nombreComboBox = new QComboBox(Form);
        nombreComboBox->setObjectName(QString::fromUtf8("nombreComboBox"));
        nombreComboBox->setGeometry(QRect(90, 50, 111, 21));
        arecomboBox = new QComboBox(Form);
        arecomboBox->setObjectName(QString::fromUtf8("arecomboBox"));
        arecomboBox->setGeometry(QRect(90, 20, 111, 21));
        alumnoComboBox = new QComboBox(Form);
        alumnoComboBox->setObjectName(QString::fromUtf8("alumnoComboBox"));
        alumnoComboBox->setGeometry(QRect(90, 140, 111, 21));
        fechaInicioDate = new QDateEdit(Form);
        fechaInicioDate->setObjectName(QString::fromUtf8("fechaInicioDate"));
        fechaInicioDate->setGeometry(QRect(90, 110, 110, 21));
        aceptarBtn = new QPushButton(Form);
        aceptarBtn->setObjectName(QString::fromUtf8("aceptarBtn"));
        aceptarBtn->setGeometry(QRect(20, 180, 75, 23));
        CancelarBtn = new QPushButton(Form);
        CancelarBtn->setObjectName(QString::fromUtf8("CancelarBtn"));
        CancelarBtn->setGeometry(QRect(130, 180, 75, 23));

        retranslateUi(Form);
        QObject::connect(aceptarBtn, SIGNAL(clicked()), Form, SLOT(agregarPersonaCurso()));
        QObject::connect(CancelarBtn, SIGNAL(clicked()), Form, SLOT(cancelar()));

        QMetaObject::connectSlotsByName(Form);
    } // setupUi

    void retranslateUi(QWidget *Form)
    {
        Form->setWindowTitle(QApplication::translate("Form", "Form", 0, QApplication::UnicodeUTF8));
        areaLbl->setText(QApplication::translate("Form", "\303\201rea:", 0, QApplication::UnicodeUTF8));
        nombreLbl->setText(QApplication::translate("Form", "Nombre:", 0, QApplication::UnicodeUTF8));
        coloniaLbl->setText(QApplication::translate("Form", "Colonia:", 0, QApplication::UnicodeUTF8));
        fechaInicioLbl->setText(QApplication::translate("Form", "Fecha Inicio:", 0, QApplication::UnicodeUTF8));
        alumnoLbl->setText(QApplication::translate("Form", "Persona:", 0, QApplication::UnicodeUTF8));
        aceptarBtn->setText(QApplication::translate("Form", " Aceptar", 0, QApplication::UnicodeUTF8));
        CancelarBtn->setText(QApplication::translate("Form", "Cancelar", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class Form: public Ui_Form {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_AGREGARPERSONACURSO_H
