/********************************************************************************
** Form generated from reading UI file 'AgregarViaDonacion.ui'
**
** Created: Mon 17. Jun 23:12:28 2013
**      by: Qt User Interface Compiler version 4.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_AGREGARVIADONACION_H
#define UI_AGREGARVIADONACION_H

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
    QLineEdit *viaDonacionTxt;
    QLabel *viaDonacionLbl;
    QPushButton *aceptarBtn;
    QPushButton *cancelarBtn;

    void setupUi(QWidget *Form)
    {
        if (Form->objectName().isEmpty())
            Form->setObjectName(QString::fromUtf8("Form"));
        Form->resize(239, 83);
        viaDonacionTxt = new QLineEdit(Form);
        viaDonacionTxt->setObjectName(QString::fromUtf8("viaDonacionTxt"));
        viaDonacionTxt->setGeometry(QRect(100, 20, 113, 20));
        viaDonacionLbl = new QLabel(Form);
        viaDonacionLbl->setObjectName(QString::fromUtf8("viaDonacionLbl"));
        viaDonacionLbl->setGeometry(QRect(20, 20, 71, 16));
        aceptarBtn = new QPushButton(Form);
        aceptarBtn->setObjectName(QString::fromUtf8("aceptarBtn"));
        aceptarBtn->setGeometry(QRect(30, 50, 75, 23));
        cancelarBtn = new QPushButton(Form);
        cancelarBtn->setObjectName(QString::fromUtf8("cancelarBtn"));
        cancelarBtn->setGeometry(QRect(140, 50, 75, 23));

        retranslateUi(Form);
        QObject::connect(aceptarBtn, SIGNAL(clicked()), Form, SLOT(agregarViaDonacion()));
        QObject::connect(cancelarBtn, SIGNAL(clicked()), Form, SLOT(cancelar()));

        QMetaObject::connectSlotsByName(Form);
    } // setupUi

    void retranslateUi(QWidget *Form)
    {
        Form->setWindowTitle(QApplication::translate("Form", "Form", 0, QApplication::UnicodeUTF8));
        viaDonacionLbl->setText(QApplication::translate("Form", "Via Donacion:", 0, QApplication::UnicodeUTF8));
        aceptarBtn->setText(QApplication::translate("Form", "Aceptar", 0, QApplication::UnicodeUTF8));
        cancelarBtn->setText(QApplication::translate("Form", "Cancelar", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class Form: public Ui_Form {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_AGREGARVIADONACION_H
