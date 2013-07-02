/********************************************************************************
** Form generated from reading UI file 'AgregarPersona.ui'
**
** Created: Mon 17. Jun 23:12:26 2013
**      by: Qt User Interface Compiler version 4.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_AGREGARPERSONA_H
#define UI_AGREGARPERSONA_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QComboBox>
#include <QtGui/QDateEdit>
#include <QtGui/QGroupBox>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QLineEdit>
#include <QtGui/QPushButton>
#include <QtGui/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Form
{
public:
    QPushButton *aceptarBtn;
    QPushButton *cancelarBtn;
    QGroupBox *groupBox;
    QLabel *amLbl;
    QLineEdit *telefonoTxt;
    QLabel *gradoEscolarLbl;
    QLabel *nombreLbl;
    QComboBox *gradoEscolarComboBox;
    QLineEdit *celularTxt;
    QLabel *generoLbl;
    QLabel *celularLbl;
    QLabel *emailLbl;
    QDateEdit *fechaNac;
    QLabel *telefonoLbl;
    QLabel *domicilioLbl;
    QLineEdit *domicilioTxt;
    QComboBox *coloniaComboBox;
    QLabel *coloniaLbl;
    QLineEdit *emailTxt;
    QLabel *codigoPostalLbl;
    QLineEdit *apTxt_2;
    QLabel *monitoreoLbl;
    QComboBox *generoComboBox;
    QLineEdit *codigoPostalTxt;
    QLabel *fechaNacLbl;
    QLineEdit *apTxt;
    QComboBox *monitoreoComboBox;
    QLineEdit *nombreTxt;
    QLabel *apLbl;
    QLabel *areaLbl;
    QLabel *puestoEscuelaLbl;
    QLabel *usuarioTelEmeLbl;
    QLabel *contrasenaNombreResLbl;
    QLabel *label_5;
    QLabel *fechaInicioLbl;
    QLabel *label_7;
    QLabel *fechaFinLbl;
    QComboBox *areaComboBox;
    QLineEdit *contrasenaNombreResTxt;
    QLineEdit *usuarioTelEmeTxt;
    QComboBox *puestoEscuelaComboBox;
    QLineEdit *lineEdit_3;
    QLineEdit *lineEdit_4;
    QDateEdit *dateEdit;
    QDateEdit *dateEdit_2;

    void setupUi(QWidget *Form)
    {
        if (Form->objectName().isEmpty())
            Form->setObjectName(QString::fromUtf8("Form"));
        Form->resize(534, 450);
        Form->setAutoFillBackground(false);
        aceptarBtn = new QPushButton(Form);
        aceptarBtn->setObjectName(QString::fromUtf8("aceptarBtn"));
        aceptarBtn->setGeometry(QRect(330, 410, 75, 23));
        cancelarBtn = new QPushButton(Form);
        cancelarBtn->setObjectName(QString::fromUtf8("cancelarBtn"));
        cancelarBtn->setGeometry(QRect(430, 410, 75, 23));
        groupBox = new QGroupBox(Form);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        groupBox->setGeometry(QRect(10, 20, 501, 371));
        amLbl = new QLabel(groupBox);
        amLbl->setObjectName(QString::fromUtf8("amLbl"));
        amLbl->setGeometry(QRect(30, 100, 81, 16));
        telefonoTxt = new QLineEdit(groupBox);
        telefonoTxt->setObjectName(QString::fromUtf8("telefonoTxt"));
        telefonoTxt->setGeometry(QRect(370, 40, 113, 21));
        gradoEscolarLbl = new QLabel(groupBox);
        gradoEscolarLbl->setObjectName(QString::fromUtf8("gradoEscolarLbl"));
        gradoEscolarLbl->setGeometry(QRect(30, 280, 81, 16));
        nombreLbl = new QLabel(groupBox);
        nombreLbl->setObjectName(QString::fromUtf8("nombreLbl"));
        nombreLbl->setGeometry(QRect(30, 40, 46, 13));
        gradoEscolarComboBox = new QComboBox(groupBox);
        gradoEscolarComboBox->setObjectName(QString::fromUtf8("gradoEscolarComboBox"));
        gradoEscolarComboBox->setGeometry(QRect(120, 280, 111, 21));
        celularTxt = new QLineEdit(groupBox);
        celularTxt->setObjectName(QString::fromUtf8("celularTxt"));
        celularTxt->setGeometry(QRect(370, 70, 113, 21));
        generoLbl = new QLabel(groupBox);
        generoLbl->setObjectName(QString::fromUtf8("generoLbl"));
        generoLbl->setGeometry(QRect(30, 130, 46, 13));
        celularLbl = new QLabel(groupBox);
        celularLbl->setObjectName(QString::fromUtf8("celularLbl"));
        celularLbl->setGeometry(QRect(270, 70, 46, 13));
        emailLbl = new QLabel(groupBox);
        emailLbl->setObjectName(QString::fromUtf8("emailLbl"));
        emailLbl->setGeometry(QRect(270, 100, 101, 16));
        fechaNac = new QDateEdit(groupBox);
        fechaNac->setObjectName(QString::fromUtf8("fechaNac"));
        fechaNac->setGeometry(QRect(120, 160, 110, 21));
        telefonoLbl = new QLabel(groupBox);
        telefonoLbl->setObjectName(QString::fromUtf8("telefonoLbl"));
        telefonoLbl->setGeometry(QRect(270, 40, 46, 13));
        domicilioLbl = new QLabel(groupBox);
        domicilioLbl->setObjectName(QString::fromUtf8("domicilioLbl"));
        domicilioLbl->setGeometry(QRect(30, 190, 46, 13));
        domicilioTxt = new QLineEdit(groupBox);
        domicilioTxt->setObjectName(QString::fromUtf8("domicilioTxt"));
        domicilioTxt->setGeometry(QRect(120, 190, 113, 21));
        coloniaComboBox = new QComboBox(groupBox);
        coloniaComboBox->setObjectName(QString::fromUtf8("coloniaComboBox"));
        coloniaComboBox->setGeometry(QRect(120, 220, 111, 21));
        coloniaLbl = new QLabel(groupBox);
        coloniaLbl->setObjectName(QString::fromUtf8("coloniaLbl"));
        coloniaLbl->setGeometry(QRect(30, 220, 46, 13));
        emailTxt = new QLineEdit(groupBox);
        emailTxt->setObjectName(QString::fromUtf8("emailTxt"));
        emailTxt->setGeometry(QRect(370, 100, 113, 21));
        codigoPostalLbl = new QLabel(groupBox);
        codigoPostalLbl->setObjectName(QString::fromUtf8("codigoPostalLbl"));
        codigoPostalLbl->setGeometry(QRect(30, 250, 71, 16));
        apTxt_2 = new QLineEdit(groupBox);
        apTxt_2->setObjectName(QString::fromUtf8("apTxt_2"));
        apTxt_2->setGeometry(QRect(120, 100, 113, 21));
        monitoreoLbl = new QLabel(groupBox);
        monitoreoLbl->setObjectName(QString::fromUtf8("monitoreoLbl"));
        monitoreoLbl->setGeometry(QRect(270, 130, 61, 16));
        generoComboBox = new QComboBox(groupBox);
        generoComboBox->setObjectName(QString::fromUtf8("generoComboBox"));
        generoComboBox->setGeometry(QRect(120, 130, 111, 21));
        codigoPostalTxt = new QLineEdit(groupBox);
        codigoPostalTxt->setObjectName(QString::fromUtf8("codigoPostalTxt"));
        codigoPostalTxt->setGeometry(QRect(120, 250, 113, 21));
        fechaNacLbl = new QLabel(groupBox);
        fechaNacLbl->setObjectName(QString::fromUtf8("fechaNacLbl"));
        fechaNacLbl->setGeometry(QRect(30, 160, 91, 16));
        apTxt = new QLineEdit(groupBox);
        apTxt->setObjectName(QString::fromUtf8("apTxt"));
        apTxt->setGeometry(QRect(120, 70, 113, 21));
        monitoreoComboBox = new QComboBox(groupBox);
        monitoreoComboBox->setObjectName(QString::fromUtf8("monitoreoComboBox"));
        monitoreoComboBox->setGeometry(QRect(370, 130, 111, 21));
        nombreTxt = new QLineEdit(groupBox);
        nombreTxt->setObjectName(QString::fromUtf8("nombreTxt"));
        nombreTxt->setGeometry(QRect(120, 40, 113, 21));
        apLbl = new QLabel(groupBox);
        apLbl->setObjectName(QString::fromUtf8("apLbl"));
        apLbl->setGeometry(QRect(30, 70, 91, 16));
        areaLbl = new QLabel(groupBox);
        areaLbl->setObjectName(QString::fromUtf8("areaLbl"));
        areaLbl->setGeometry(QRect(270, 160, 46, 13));
        puestoEscuelaLbl = new QLabel(groupBox);
        puestoEscuelaLbl->setObjectName(QString::fromUtf8("puestoEscuelaLbl"));
        puestoEscuelaLbl->setGeometry(QRect(270, 190, 46, 13));
        usuarioTelEmeLbl = new QLabel(groupBox);
        usuarioTelEmeLbl->setObjectName(QString::fromUtf8("usuarioTelEmeLbl"));
        usuarioTelEmeLbl->setGeometry(QRect(270, 220, 46, 13));
        contrasenaNombreResLbl = new QLabel(groupBox);
        contrasenaNombreResLbl->setObjectName(QString::fromUtf8("contrasenaNombreResLbl"));
        contrasenaNombreResLbl->setGeometry(QRect(270, 250, 46, 13));
        label_5 = new QLabel(groupBox);
        label_5->setObjectName(QString::fromUtf8("label_5"));
        label_5->setGeometry(QRect(270, 280, 91, 16));
        fechaInicioLbl = new QLabel(groupBox);
        fechaInicioLbl->setObjectName(QString::fromUtf8("fechaInicioLbl"));
        fechaInicioLbl->setGeometry(QRect(30, 310, 71, 16));
        label_7 = new QLabel(groupBox);
        label_7->setObjectName(QString::fromUtf8("label_7"));
        label_7->setGeometry(QRect(270, 310, 101, 16));
        fechaFinLbl = new QLabel(groupBox);
        fechaFinLbl->setObjectName(QString::fromUtf8("fechaFinLbl"));
        fechaFinLbl->setGeometry(QRect(30, 340, 61, 16));
        areaComboBox = new QComboBox(groupBox);
        areaComboBox->setObjectName(QString::fromUtf8("areaComboBox"));
        areaComboBox->setGeometry(QRect(370, 160, 111, 22));
        contrasenaNombreResTxt = new QLineEdit(groupBox);
        contrasenaNombreResTxt->setObjectName(QString::fromUtf8("contrasenaNombreResTxt"));
        contrasenaNombreResTxt->setGeometry(QRect(370, 250, 113, 20));
        usuarioTelEmeTxt = new QLineEdit(groupBox);
        usuarioTelEmeTxt->setObjectName(QString::fromUtf8("usuarioTelEmeTxt"));
        usuarioTelEmeTxt->setGeometry(QRect(370, 220, 113, 20));
        puestoEscuelaComboBox = new QComboBox(groupBox);
        puestoEscuelaComboBox->setObjectName(QString::fromUtf8("puestoEscuelaComboBox"));
        puestoEscuelaComboBox->setGeometry(QRect(370, 190, 111, 22));
        lineEdit_3 = new QLineEdit(groupBox);
        lineEdit_3->setObjectName(QString::fromUtf8("lineEdit_3"));
        lineEdit_3->setGeometry(QRect(370, 280, 113, 20));
        lineEdit_4 = new QLineEdit(groupBox);
        lineEdit_4->setObjectName(QString::fromUtf8("lineEdit_4"));
        lineEdit_4->setGeometry(QRect(370, 310, 113, 20));
        dateEdit = new QDateEdit(groupBox);
        dateEdit->setObjectName(QString::fromUtf8("dateEdit"));
        dateEdit->setGeometry(QRect(120, 310, 110, 21));
        dateEdit_2 = new QDateEdit(groupBox);
        dateEdit_2->setObjectName(QString::fromUtf8("dateEdit_2"));
        dateEdit_2->setGeometry(QRect(120, 340, 110, 21));
        aceptarBtn->raise();
        cancelarBtn->raise();
        groupBox->raise();
        monitoreoComboBox->raise();
        emailTxt->raise();
        monitoreoLbl->raise();
        emailLbl->raise();

        retranslateUi(Form);
        QObject::connect(aceptarBtn, SIGNAL(clicked()), Form, SLOT(agregarPersona()));
        QObject::connect(cancelarBtn, SIGNAL(clicked()), Form, SLOT(cancelar()));

        QMetaObject::connectSlotsByName(Form);
    } // setupUi

    void retranslateUi(QWidget *Form)
    {
        Form->setWindowTitle(QApplication::translate("Form", "Form", 0, QApplication::UnicodeUTF8));
        aceptarBtn->setText(QApplication::translate("Form", "Aceptar", 0, QApplication::UnicodeUTF8));
        cancelarBtn->setText(QApplication::translate("Form", "Cancelar", 0, QApplication::UnicodeUTF8));
        groupBox->setTitle(QApplication::translate("Form", "Datos Persona", 0, QApplication::UnicodeUTF8));
        amLbl->setText(QApplication::translate("Form", "Apellid Paterno:", 0, QApplication::UnicodeUTF8));
        gradoEscolarLbl->setText(QApplication::translate("Form", "Grado Escolar:", 0, QApplication::UnicodeUTF8));
        nombreLbl->setText(QApplication::translate("Form", "Nombre:", 0, QApplication::UnicodeUTF8));
        generoLbl->setText(QApplication::translate("Form", "Genero:", 0, QApplication::UnicodeUTF8));
        celularLbl->setText(QApplication::translate("Form", "Celular:", 0, QApplication::UnicodeUTF8));
        emailLbl->setText(QApplication::translate("Form", "E-Mail:", 0, QApplication::UnicodeUTF8));
        telefonoLbl->setText(QApplication::translate("Form", "Telefono:", 0, QApplication::UnicodeUTF8));
        domicilioLbl->setText(QApplication::translate("Form", "Domicilio:", 0, QApplication::UnicodeUTF8));
        coloniaLbl->setText(QApplication::translate("Form", "Colonia:", 0, QApplication::UnicodeUTF8));
        codigoPostalLbl->setText(QApplication::translate("Form", "Codigo Postal:", 0, QApplication::UnicodeUTF8));
        monitoreoLbl->setText(QApplication::translate("Form", "Monitoreo:", 0, QApplication::UnicodeUTF8));
        fechaNacLbl->setText(QApplication::translate("Form", "Fecha Nacimiento:", 0, QApplication::UnicodeUTF8));
        apLbl->setText(QApplication::translate("Form", "Apellido Materno:", 0, QApplication::UnicodeUTF8));
        areaLbl->setText(QApplication::translate("Form", "\303\201rea:", 0, QApplication::UnicodeUTF8));
        puestoEscuelaLbl->setText(QApplication::translate("Form", "temp", 0, QApplication::UnicodeUTF8));
        usuarioTelEmeLbl->setText(QApplication::translate("Form", "temp", 0, QApplication::UnicodeUTF8));
        contrasenaNombreResLbl->setText(QApplication::translate("Form", "temp", 0, QApplication::UnicodeUTF8));
        label_5->setText(QApplication::translate("Form", "Tel. Responsable:", 0, QApplication::UnicodeUTF8));
        fechaInicioLbl->setText(QApplication::translate("Form", "Fecha inicio:", 0, QApplication::UnicodeUTF8));
        label_7->setText(QApplication::translate("Form", "E-Mail Responsable:", 0, QApplication::UnicodeUTF8));
        fechaFinLbl->setText(QApplication::translate("Form", "Fecha fin:", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class Form: public Ui_Form {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_AGREGARPERSONA_H
