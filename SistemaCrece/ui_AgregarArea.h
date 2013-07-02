/********************************************************************************
** Form generated from reading UI file 'AgregarArea.ui'
**
** Created: Mon 17. Jun 23:12:26 2013
**      by: Qt User Interface Compiler version 4.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_AGREGARAREA_H
#define UI_AGREGARAREA_H

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
    QLabel *areaLbl;
    QLineEdit *areaTxt;
    QPushButton *aceptarBtn;
    QPushButton *cancelarBtn;

    void setupUi(QWidget *Form)
    {
        if (Form->objectName().isEmpty())
            Form->setObjectName(QString::fromUtf8("Form"));
        Form->resize(200, 94);
        areaLbl = new QLabel(Form);
        areaLbl->setObjectName(QString::fromUtf8("areaLbl"));
        areaLbl->setGeometry(QRect(20, 20, 46, 13));
        areaTxt = new QLineEdit(Form);
        areaTxt->setObjectName(QString::fromUtf8("areaTxt"));
        areaTxt->setGeometry(QRect(60, 20, 121, 20));
        aceptarBtn = new QPushButton(Form);
        aceptarBtn->setObjectName(QString::fromUtf8("aceptarBtn"));
        aceptarBtn->setGeometry(QRect(10, 60, 75, 23));
        cancelarBtn = new QPushButton(Form);
        cancelarBtn->setObjectName(QString::fromUtf8("cancelarBtn"));
        cancelarBtn->setGeometry(QRect(110, 60, 75, 23));

        retranslateUi(Form);
        QObject::connect(aceptarBtn, SIGNAL(clicked()), Form, SLOT(agregarArea()));
        QObject::connect(cancelarBtn, SIGNAL(clicked()), Form, SLOT(cancelar()));

        QMetaObject::connectSlotsByName(Form);
    } // setupUi

    void retranslateUi(QWidget *Form)
    {
        Form->setWindowTitle(QApplication::translate("Form", "Form", 0, QApplication::UnicodeUTF8));
        areaLbl->setText(QApplication::translate("Form", "\303\201rea:", 0, QApplication::UnicodeUTF8));
        aceptarBtn->setText(QApplication::translate("Form", "Aceptar", 0, QApplication::UnicodeUTF8));
        cancelarBtn->setText(QApplication::translate("Form", "Cancelar", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class Form: public Ui_Form {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_AGREGARAREA_H
