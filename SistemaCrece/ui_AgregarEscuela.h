/********************************************************************************
** Form generated from reading UI file 'AgregarEscuela.ui'
**
** Created: Mon 17. Jun 23:12:27 2013
**      by: Qt User Interface Compiler version 4.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_AGREGARESCUELA_H
#define UI_AGREGARESCUELA_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QComboBox>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QLineEdit>
#include <QtGui/QPushButton>
#include <QtGui/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Form
{
public:
    QLabel *nombreLbl;
    QLabel *domicilioLbl;
    QLabel *codigoPostalLbl;
    QLabel *telefonoLbl;
    QLabel *coloniaLbl;
    QLineEdit *codigoPostalTxt;
    QLineEdit *nombreTxt;
    QLineEdit *domicilioTxt;
    QLineEdit *telefonoTxt;
    QComboBox *ColoniaComboBox;
    QPushButton *aceptarBtn;
    QPushButton *cancelarBtnb;

    void setupUi(QWidget *Form)
    {
        if (Form->objectName().isEmpty())
            Form->setObjectName(QString::fromUtf8("Form"));
        Form->resize(233, 216);
        nombreLbl = new QLabel(Form);
        nombreLbl->setObjectName(QString::fromUtf8("nombreLbl"));
        nombreLbl->setGeometry(QRect(20, 20, 46, 13));
        domicilioLbl = new QLabel(Form);
        domicilioLbl->setObjectName(QString::fromUtf8("domicilioLbl"));
        domicilioLbl->setGeometry(QRect(20, 50, 46, 13));
        codigoPostalLbl = new QLabel(Form);
        codigoPostalLbl->setObjectName(QString::fromUtf8("codigoPostalLbl"));
        codigoPostalLbl->setGeometry(QRect(20, 80, 71, 16));
        telefonoLbl = new QLabel(Form);
        telefonoLbl->setObjectName(QString::fromUtf8("telefonoLbl"));
        telefonoLbl->setGeometry(QRect(20, 110, 46, 13));
        coloniaLbl = new QLabel(Form);
        coloniaLbl->setObjectName(QString::fromUtf8("coloniaLbl"));
        coloniaLbl->setGeometry(QRect(20, 140, 46, 13));
        codigoPostalTxt = new QLineEdit(Form);
        codigoPostalTxt->setObjectName(QString::fromUtf8("codigoPostalTxt"));
        codigoPostalTxt->setGeometry(QRect(100, 80, 113, 20));
        nombreTxt = new QLineEdit(Form);
        nombreTxt->setObjectName(QString::fromUtf8("nombreTxt"));
        nombreTxt->setGeometry(QRect(100, 20, 113, 20));
        domicilioTxt = new QLineEdit(Form);
        domicilioTxt->setObjectName(QString::fromUtf8("domicilioTxt"));
        domicilioTxt->setGeometry(QRect(100, 50, 113, 20));
        telefonoTxt = new QLineEdit(Form);
        telefonoTxt->setObjectName(QString::fromUtf8("telefonoTxt"));
        telefonoTxt->setGeometry(QRect(100, 110, 113, 20));
        ColoniaComboBox = new QComboBox(Form);
        ColoniaComboBox->setObjectName(QString::fromUtf8("ColoniaComboBox"));
        ColoniaComboBox->setGeometry(QRect(100, 140, 111, 21));
        aceptarBtn = new QPushButton(Form);
        aceptarBtn->setObjectName(QString::fromUtf8("aceptarBtn"));
        aceptarBtn->setGeometry(QRect(30, 180, 75, 23));
        cancelarBtnb = new QPushButton(Form);
        cancelarBtnb->setObjectName(QString::fromUtf8("cancelarBtnb"));
        cancelarBtnb->setGeometry(QRect(140, 180, 75, 23));

        retranslateUi(Form);
        QObject::connect(aceptarBtn, SIGNAL(clicked()), Form, SLOT(agregarEscuela()));
        QObject::connect(cancelarBtnb, SIGNAL(clicked()), Form, SLOT(cancelar()));

        QMetaObject::connectSlotsByName(Form);
    } // setupUi

    void retranslateUi(QWidget *Form)
    {
        Form->setWindowTitle(QApplication::translate("Form", "Form", 0, QApplication::UnicodeUTF8));
        nombreLbl->setText(QApplication::translate("Form", "Nombre:", 0, QApplication::UnicodeUTF8));
        domicilioLbl->setText(QApplication::translate("Form", "Domicilio:", 0, QApplication::UnicodeUTF8));
        codigoPostalLbl->setText(QApplication::translate("Form", "Codigo Postal:", 0, QApplication::UnicodeUTF8));
        telefonoLbl->setText(QApplication::translate("Form", "Telefono:", 0, QApplication::UnicodeUTF8));
        coloniaLbl->setText(QApplication::translate("Form", "Colonia:", 0, QApplication::UnicodeUTF8));
        aceptarBtn->setText(QApplication::translate("Form", "Aceptar", 0, QApplication::UnicodeUTF8));
        cancelarBtnb->setText(QApplication::translate("Form", "Cancelar", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class Form: public Ui_Form {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_AGREGARESCUELA_H
