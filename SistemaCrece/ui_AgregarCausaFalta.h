/********************************************************************************
** Form generated from reading UI file 'AgregarCausaFalta.ui'
**
** Created: Mon 17. Jun 23:12:26 2013
**      by: Qt User Interface Compiler version 4.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_AGREGARCAUSAFALTA_H
#define UI_AGREGARCAUSAFALTA_H

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
    QLabel *causaLbl;
    QLabel *descripcionLbl;
    QLineEdit *causaTxt;
    QLineEdit *descripcionTxt;
    QPushButton *aceptarBtn;
    QPushButton *cancelarBtn;

    void setupUi(QWidget *Form)
    {
        if (Form->objectName().isEmpty())
            Form->setObjectName(QString::fromUtf8("Form"));
        Form->resize(212, 116);
        causaLbl = new QLabel(Form);
        causaLbl->setObjectName(QString::fromUtf8("causaLbl"));
        causaLbl->setGeometry(QRect(20, 20, 46, 13));
        descripcionLbl = new QLabel(Form);
        descripcionLbl->setObjectName(QString::fromUtf8("descripcionLbl"));
        descripcionLbl->setGeometry(QRect(20, 50, 61, 16));
        causaTxt = new QLineEdit(Form);
        causaTxt->setObjectName(QString::fromUtf8("causaTxt"));
        causaTxt->setGeometry(QRect(90, 20, 113, 20));
        descripcionTxt = new QLineEdit(Form);
        descripcionTxt->setObjectName(QString::fromUtf8("descripcionTxt"));
        descripcionTxt->setGeometry(QRect(90, 50, 113, 20));
        aceptarBtn = new QPushButton(Form);
        aceptarBtn->setObjectName(QString::fromUtf8("aceptarBtn"));
        aceptarBtn->setGeometry(QRect(30, 80, 75, 23));
        cancelarBtn = new QPushButton(Form);
        cancelarBtn->setObjectName(QString::fromUtf8("cancelarBtn"));
        cancelarBtn->setGeometry(QRect(130, 80, 75, 23));

        retranslateUi(Form);
        QObject::connect(aceptarBtn, SIGNAL(clicked()), Form, SLOT(agregarCausaFalta()));
        QObject::connect(cancelarBtn, SIGNAL(clicked()), Form, SLOT(cancelar()));

        QMetaObject::connectSlotsByName(Form);
    } // setupUi

    void retranslateUi(QWidget *Form)
    {
        Form->setWindowTitle(QApplication::translate("Form", "Form", 0, QApplication::UnicodeUTF8));
        causaLbl->setText(QApplication::translate("Form", "Causa:", 0, QApplication::UnicodeUTF8));
        descripcionLbl->setText(QApplication::translate("Form", "Descripci\303\263n:", 0, QApplication::UnicodeUTF8));
        aceptarBtn->setText(QApplication::translate("Form", "Aceptar", 0, QApplication::UnicodeUTF8));
        cancelarBtn->setText(QApplication::translate("Form", "Cancelar", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class Form: public Ui_Form {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_AGREGARCAUSAFALTA_H
