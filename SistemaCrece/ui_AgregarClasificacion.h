/********************************************************************************
** Form generated from reading UI file 'AgregarClasificacion.ui'
**
** Created: Mon 17. Jun 23:12:27 2013
**      by: Qt User Interface Compiler version 4.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_AGREGARCLASIFICACION_H
#define UI_AGREGARCLASIFICACION_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QLineEdit>
#include <QtGui/QPushButton>
#include <QtGui/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Form
{
public:
    QLabel *clasificacionLbl;
    QLineEdit *clasificacionTxt;
    QPushButton *aceptarBtn;
    QPushButton *cancelarBtn;

    void setupUi(QWidget *Form)
    {
        if (Form->objectName().isEmpty())
            Form->setObjectName(QString::fromUtf8("Form"));
        Form->resize(224, 89);
        clasificacionLbl = new QLabel(Form);
        clasificacionLbl->setObjectName(QString::fromUtf8("clasificacionLbl"));
        clasificacionLbl->setGeometry(QRect(20, 10, 71, 16));
        clasificacionTxt = new QLineEdit(Form);
        clasificacionTxt->setObjectName(QString::fromUtf8("clasificacionTxt"));
        clasificacionTxt->setGeometry(QRect(90, 10, 113, 20));
        aceptarBtn = new QPushButton(Form);
        aceptarBtn->setObjectName(QString::fromUtf8("aceptarBtn"));
        aceptarBtn->setGeometry(QRect(30, 50, 75, 23));
        cancelarBtn = new QPushButton(Form);
        cancelarBtn->setObjectName(QString::fromUtf8("cancelarBtn"));
        cancelarBtn->setGeometry(QRect(130, 50, 75, 23));

        retranslateUi(Form);
        QObject::connect(aceptarBtn, SIGNAL(clicked()), Form, SLOT(agregarClasificacion()));
        QObject::connect(cancelarBtn, SIGNAL(clicked()), Form, SLOT(cancelar()));

        QMetaObject::connectSlotsByName(Form);
    } // setupUi

    void retranslateUi(QWidget *Form)
    {
        Form->setWindowTitle(QApplication::translate("Form", "Form", 0, QApplication::UnicodeUTF8));
        clasificacionLbl->setText(QApplication::translate("Form", "Clasificaci\303\263n:", 0, QApplication::UnicodeUTF8));
        aceptarBtn->setText(QApplication::translate("Form", "Aceptar", 0, QApplication::UnicodeUTF8));
        cancelarBtn->setText(QApplication::translate("Form", "Cancelar", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class Form: public Ui_Form {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_AGREGARCLASIFICACION_H
