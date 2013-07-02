/********************************************************************************
** Form generated from reading UI file 'EscojerCurso.ui'
**
** Created: Mon 17. Jun 23:12:28 2013
**      by: Qt User Interface Compiler version 4.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_ESCOJERCURSO_H
#define UI_ESCOJERCURSO_H

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
    QDateEdit *fechaInicioDate;
    QLabel *nombreLbl;
    QPushButton *aceptarBtn;
    QLabel *areaLbl;
    QComboBox *nombreComboBox;
    QLabel *coloniaLbl;
    QLabel *fechaInicioLbl;
    QComboBox *arecomboBox;
    QComboBox *coloniaComboBox;

    void setupUi(QWidget *Form)
    {
        if (Form->objectName().isEmpty())
            Form->setObjectName(QString::fromUtf8("Form"));
        Form->resize(228, 173);
        fechaInicioDate = new QDateEdit(Form);
        fechaInicioDate->setObjectName(QString::fromUtf8("fechaInicioDate"));
        fechaInicioDate->setGeometry(QRect(90, 100, 110, 21));
        nombreLbl = new QLabel(Form);
        nombreLbl->setObjectName(QString::fromUtf8("nombreLbl"));
        nombreLbl->setGeometry(QRect(20, 40, 46, 13));
        aceptarBtn = new QPushButton(Form);
        aceptarBtn->setObjectName(QString::fromUtf8("aceptarBtn"));
        aceptarBtn->setGeometry(QRect(130, 130, 75, 23));
        areaLbl = new QLabel(Form);
        areaLbl->setObjectName(QString::fromUtf8("areaLbl"));
        areaLbl->setGeometry(QRect(20, 10, 46, 13));
        nombreComboBox = new QComboBox(Form);
        nombreComboBox->setObjectName(QString::fromUtf8("nombreComboBox"));
        nombreComboBox->setGeometry(QRect(90, 40, 111, 21));
        coloniaLbl = new QLabel(Form);
        coloniaLbl->setObjectName(QString::fromUtf8("coloniaLbl"));
        coloniaLbl->setGeometry(QRect(20, 70, 46, 13));
        fechaInicioLbl = new QLabel(Form);
        fechaInicioLbl->setObjectName(QString::fromUtf8("fechaInicioLbl"));
        fechaInicioLbl->setGeometry(QRect(20, 100, 61, 16));
        arecomboBox = new QComboBox(Form);
        arecomboBox->setObjectName(QString::fromUtf8("arecomboBox"));
        arecomboBox->setGeometry(QRect(90, 10, 111, 21));
        coloniaComboBox = new QComboBox(Form);
        coloniaComboBox->setObjectName(QString::fromUtf8("coloniaComboBox"));
        coloniaComboBox->setGeometry(QRect(90, 70, 111, 21));

        retranslateUi(Form);
        QObject::connect(aceptarBtn, SIGNAL(clicked()), Form, SLOT(escojerCurso()));
        QObject::connect(aceptarBtn, SIGNAL(clicked()), Form, SLOT(cancelar()));

        QMetaObject::connectSlotsByName(Form);
    } // setupUi

    void retranslateUi(QWidget *Form)
    {
        Form->setWindowTitle(QApplication::translate("Form", "Form", 0, QApplication::UnicodeUTF8));
        nombreLbl->setText(QApplication::translate("Form", "Nombre:", 0, QApplication::UnicodeUTF8));
        aceptarBtn->setText(QApplication::translate("Form", " Aceptar", 0, QApplication::UnicodeUTF8));
        areaLbl->setText(QApplication::translate("Form", "\303\201rea:", 0, QApplication::UnicodeUTF8));
        coloniaLbl->setText(QApplication::translate("Form", "Colonia:", 0, QApplication::UnicodeUTF8));
        fechaInicioLbl->setText(QApplication::translate("Form", "Fecha Inicio:", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class Form: public Ui_Form {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_ESCOJERCURSO_H
