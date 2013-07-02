/********************************************************************************
** Form generated from reading UI file 'Inicio.ui'
**
** Created: Mon 17. Jun 23:12:26 2013
**      by: Qt User Interface Compiler version 4.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_INICIO_H
#define UI_INICIO_H

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

class Ui_contrasenaLbl
{
public:
    QLabel *usuarioLbl;
    QLabel *label_2;
    QPushButton *ingresarBtn;
    QLineEdit *lineEdit;
    QLineEdit *lineEdit_2;

    void setupUi(QWidget *contrasenaLbl)
    {
        if (contrasenaLbl->objectName().isEmpty())
            contrasenaLbl->setObjectName(QString::fromUtf8("contrasenaLbl"));
        contrasenaLbl->resize(214, 127);
        usuarioLbl = new QLabel(contrasenaLbl);
        usuarioLbl->setObjectName(QString::fromUtf8("usuarioLbl"));
        usuarioLbl->setGeometry(QRect(20, 30, 46, 13));
        label_2 = new QLabel(contrasenaLbl);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setGeometry(QRect(20, 60, 61, 16));
        ingresarBtn = new QPushButton(contrasenaLbl);
        ingresarBtn->setObjectName(QString::fromUtf8("ingresarBtn"));
        ingresarBtn->setGeometry(QRect(130, 90, 75, 23));
        lineEdit = new QLineEdit(contrasenaLbl);
        lineEdit->setObjectName(QString::fromUtf8("lineEdit"));
        lineEdit->setGeometry(QRect(90, 30, 113, 20));
        lineEdit_2 = new QLineEdit(contrasenaLbl);
        lineEdit_2->setObjectName(QString::fromUtf8("lineEdit_2"));
        lineEdit_2->setGeometry(QRect(90, 60, 113, 20));
        lineEdit_2->setEchoMode(QLineEdit::PasswordEchoOnEdit);

        retranslateUi(contrasenaLbl);
        QObject::connect(ingresarBtn, SIGNAL(clicked()), contrasenaLbl, SLOT(ingresar()));

        QMetaObject::connectSlotsByName(contrasenaLbl);
    } // setupUi

    void retranslateUi(QWidget *contrasenaLbl)
    {
        contrasenaLbl->setWindowTitle(QApplication::translate("contrasenaLbl", "Form", 0, QApplication::UnicodeUTF8));
        usuarioLbl->setText(QApplication::translate("contrasenaLbl", "Usuario:", 0, QApplication::UnicodeUTF8));
        label_2->setText(QApplication::translate("contrasenaLbl", "Contrase\303\261a:", 0, QApplication::UnicodeUTF8));
        ingresarBtn->setText(QApplication::translate("contrasenaLbl", "Ingresar", 0, QApplication::UnicodeUTF8));
        lineEdit_2->setInputMask(QString());
    } // retranslateUi

};

namespace Ui {
    class contrasenaLbl: public Ui_contrasenaLbl {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_INICIO_H
