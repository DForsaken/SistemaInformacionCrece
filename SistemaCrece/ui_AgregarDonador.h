/********************************************************************************
** Form generated from reading UI file 'AgregarDonador.ui'
**
** Created: Mon 17. Jun 23:12:27 2013
**      by: Qt User Interface Compiler version 4.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_AGREGARDONADOR_H
#define UI_AGREGARDONADOR_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QComboBox>
#include <QtGui/QDateEdit>
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
    QLabel *direccionLbl;
    QLabel *telefonoLbl;
    QLabel *emailLbl;
    QLabel *clasificacionLbl;
    QLabel *viaDonacionLbl;
    QLabel *cantidadLbl;
    QLabel *fechaSalidaLbl;
    QLabel *fechaInicioLbl;
    QLineEdit *cantidadLbl_2;
    QLineEdit *nombreTxt;
    QLineEdit *direccionTxt;
    QLineEdit *telefonoTxt;
    QLineEdit *emailTxt;
    QComboBox *clasificacionComboBox;
    QComboBox *viaDonacionComboBox_2;
    QDateEdit *fechaInicioDate;
    QDateEdit *fechaFinDate;
    QPushButton *AceptarBtn;
    QPushButton *CancelarBtn;

    void setupUi(QWidget *Form)
    {
        if (Form->objectName().isEmpty())
            Form->setObjectName(QString::fromUtf8("Form"));
        Form->resize(221, 329);
        nombreLbl = new QLabel(Form);
        nombreLbl->setObjectName(QString::fromUtf8("nombreLbl"));
        nombreLbl->setGeometry(QRect(20, 20, 71, 16));
        direccionLbl = new QLabel(Form);
        direccionLbl->setObjectName(QString::fromUtf8("direccionLbl"));
        direccionLbl->setGeometry(QRect(20, 50, 46, 13));
        telefonoLbl = new QLabel(Form);
        telefonoLbl->setObjectName(QString::fromUtf8("telefonoLbl"));
        telefonoLbl->setGeometry(QRect(20, 80, 51, 16));
        emailLbl = new QLabel(Form);
        emailLbl->setObjectName(QString::fromUtf8("emailLbl"));
        emailLbl->setGeometry(QRect(20, 110, 46, 13));
        clasificacionLbl = new QLabel(Form);
        clasificacionLbl->setObjectName(QString::fromUtf8("clasificacionLbl"));
        clasificacionLbl->setGeometry(QRect(20, 140, 61, 16));
        viaDonacionLbl = new QLabel(Form);
        viaDonacionLbl->setObjectName(QString::fromUtf8("viaDonacionLbl"));
        viaDonacionLbl->setGeometry(QRect(20, 170, 71, 16));
        cantidadLbl = new QLabel(Form);
        cantidadLbl->setObjectName(QString::fromUtf8("cantidadLbl"));
        cantidadLbl->setGeometry(QRect(20, 200, 51, 16));
        fechaSalidaLbl = new QLabel(Form);
        fechaSalidaLbl->setObjectName(QString::fromUtf8("fechaSalidaLbl"));
        fechaSalidaLbl->setGeometry(QRect(20, 230, 71, 16));
        fechaInicioLbl = new QLabel(Form);
        fechaInicioLbl->setObjectName(QString::fromUtf8("fechaInicioLbl"));
        fechaInicioLbl->setGeometry(QRect(20, 260, 61, 16));
        cantidadLbl_2 = new QLineEdit(Form);
        cantidadLbl_2->setObjectName(QString::fromUtf8("cantidadLbl_2"));
        cantidadLbl_2->setGeometry(QRect(90, 200, 113, 20));
        nombreTxt = new QLineEdit(Form);
        nombreTxt->setObjectName(QString::fromUtf8("nombreTxt"));
        nombreTxt->setGeometry(QRect(90, 20, 113, 20));
        direccionTxt = new QLineEdit(Form);
        direccionTxt->setObjectName(QString::fromUtf8("direccionTxt"));
        direccionTxt->setGeometry(QRect(90, 50, 113, 20));
        telefonoTxt = new QLineEdit(Form);
        telefonoTxt->setObjectName(QString::fromUtf8("telefonoTxt"));
        telefonoTxt->setGeometry(QRect(90, 80, 113, 20));
        emailTxt = new QLineEdit(Form);
        emailTxt->setObjectName(QString::fromUtf8("emailTxt"));
        emailTxt->setGeometry(QRect(90, 110, 113, 20));
        clasificacionComboBox = new QComboBox(Form);
        clasificacionComboBox->setObjectName(QString::fromUtf8("clasificacionComboBox"));
        clasificacionComboBox->setGeometry(QRect(90, 140, 111, 21));
        viaDonacionComboBox_2 = new QComboBox(Form);
        viaDonacionComboBox_2->setObjectName(QString::fromUtf8("viaDonacionComboBox_2"));
        viaDonacionComboBox_2->setGeometry(QRect(90, 170, 111, 21));
        fechaInicioDate = new QDateEdit(Form);
        fechaInicioDate->setObjectName(QString::fromUtf8("fechaInicioDate"));
        fechaInicioDate->setGeometry(QRect(90, 230, 110, 21));
        fechaFinDate = new QDateEdit(Form);
        fechaFinDate->setObjectName(QString::fromUtf8("fechaFinDate"));
        fechaFinDate->setGeometry(QRect(90, 260, 110, 21));
        AceptarBtn = new QPushButton(Form);
        AceptarBtn->setObjectName(QString::fromUtf8("AceptarBtn"));
        AceptarBtn->setGeometry(QRect(20, 290, 75, 23));
        CancelarBtn = new QPushButton(Form);
        CancelarBtn->setObjectName(QString::fromUtf8("CancelarBtn"));
        CancelarBtn->setGeometry(QRect(130, 290, 75, 23));

        retranslateUi(Form);
        QObject::connect(AceptarBtn, SIGNAL(clicked()), Form, SLOT(agregarDonador()));
        QObject::connect(CancelarBtn, SIGNAL(clicked()), Form, SLOT(cancelar()));

        QMetaObject::connectSlotsByName(Form);
    } // setupUi

    void retranslateUi(QWidget *Form)
    {
        Form->setWindowTitle(QApplication::translate("Form", "Form", 0, QApplication::UnicodeUTF8));
        nombreLbl->setText(QApplication::translate("Form", "Nombre:", 0, QApplication::UnicodeUTF8));
        direccionLbl->setText(QApplication::translate("Form", "Direcci\303\263n:", 0, QApplication::UnicodeUTF8));
        telefonoLbl->setText(QApplication::translate("Form", "Telefono:", 0, QApplication::UnicodeUTF8));
        emailLbl->setText(QApplication::translate("Form", "E-Mail:", 0, QApplication::UnicodeUTF8));
        clasificacionLbl->setText(QApplication::translate("Form", "Clasificaci\303\263n:", 0, QApplication::UnicodeUTF8));
        viaDonacionLbl->setText(QApplication::translate("Form", "V\303\255a Donaci\303\263n:", 0, QApplication::UnicodeUTF8));
        cantidadLbl->setText(QApplication::translate("Form", "Cantdidad:", 0, QApplication::UnicodeUTF8));
        fechaSalidaLbl->setText(QApplication::translate("Form", "Fecha Salida:", 0, QApplication::UnicodeUTF8));
        fechaInicioLbl->setText(QApplication::translate("Form", "Fecha Inicio:", 0, QApplication::UnicodeUTF8));
        AceptarBtn->setText(QApplication::translate("Form", "Aceptar", 0, QApplication::UnicodeUTF8));
        CancelarBtn->setText(QApplication::translate("Form", "Cancelar", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class Form: public Ui_Form {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_AGREGARDONADOR_H
