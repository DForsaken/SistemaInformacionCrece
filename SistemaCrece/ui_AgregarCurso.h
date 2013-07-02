/********************************************************************************
** Form generated from reading UI file 'AgregarCurso.ui'
**
** Created: Mon 17. Jun 23:12:27 2013
**      by: Qt User Interface Compiler version 4.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_AGREGARCURSO_H
#define UI_AGREGARCURSO_H

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
#include <QtGui/QTextEdit>
#include <QtGui/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Form
{
public:
    QLabel *nombreLbl;
    QLabel *coloniaLbl;
    QLabel *areaLbl;
    QLabel *fechaInicioLbl;
    QLabel *fechaFinLbl;
    QLabel *enfoqueLbl;
    QLineEdit *nombreTxt;
    QTextEdit *enfoqueTxt;
    QDateEdit *fechaInicioDate;
    QDateEdit *fechaFinDate;
    QComboBox *areaComboBox;
    QComboBox *coloniaComboBox;
    QPushButton *aceptarBtn;
    QPushButton *cancelarBtn;

    void setupUi(QWidget *Form)
    {
        if (Form->objectName().isEmpty())
            Form->setObjectName(QString::fromUtf8("Form"));
        Form->resize(228, 319);
        nombreLbl = new QLabel(Form);
        nombreLbl->setObjectName(QString::fromUtf8("nombreLbl"));
        nombreLbl->setGeometry(QRect(20, 20, 46, 13));
        coloniaLbl = new QLabel(Form);
        coloniaLbl->setObjectName(QString::fromUtf8("coloniaLbl"));
        coloniaLbl->setGeometry(QRect(20, 50, 46, 13));
        areaLbl = new QLabel(Form);
        areaLbl->setObjectName(QString::fromUtf8("areaLbl"));
        areaLbl->setGeometry(QRect(20, 80, 46, 13));
        fechaInicioLbl = new QLabel(Form);
        fechaInicioLbl->setObjectName(QString::fromUtf8("fechaInicioLbl"));
        fechaInicioLbl->setGeometry(QRect(20, 110, 61, 16));
        fechaFinLbl = new QLabel(Form);
        fechaFinLbl->setObjectName(QString::fromUtf8("fechaFinLbl"));
        fechaFinLbl->setGeometry(QRect(20, 140, 61, 16));
        enfoqueLbl = new QLabel(Form);
        enfoqueLbl->setObjectName(QString::fromUtf8("enfoqueLbl"));
        enfoqueLbl->setGeometry(QRect(20, 170, 46, 13));
        nombreTxt = new QLineEdit(Form);
        nombreTxt->setObjectName(QString::fromUtf8("nombreTxt"));
        nombreTxt->setGeometry(QRect(90, 20, 113, 20));
        enfoqueTxt = new QTextEdit(Form);
        enfoqueTxt->setObjectName(QString::fromUtf8("enfoqueTxt"));
        enfoqueTxt->setGeometry(QRect(90, 170, 111, 91));
        fechaInicioDate = new QDateEdit(Form);
        fechaInicioDate->setObjectName(QString::fromUtf8("fechaInicioDate"));
        fechaInicioDate->setGeometry(QRect(90, 140, 110, 21));
        fechaFinDate = new QDateEdit(Form);
        fechaFinDate->setObjectName(QString::fromUtf8("fechaFinDate"));
        fechaFinDate->setGeometry(QRect(90, 110, 110, 21));
        areaComboBox = new QComboBox(Form);
        areaComboBox->setObjectName(QString::fromUtf8("areaComboBox"));
        areaComboBox->setGeometry(QRect(90, 80, 111, 22));
        coloniaComboBox = new QComboBox(Form);
        coloniaComboBox->setObjectName(QString::fromUtf8("coloniaComboBox"));
        coloniaComboBox->setGeometry(QRect(90, 50, 111, 22));
        aceptarBtn = new QPushButton(Form);
        aceptarBtn->setObjectName(QString::fromUtf8("aceptarBtn"));
        aceptarBtn->setGeometry(QRect(20, 280, 75, 23));
        cancelarBtn = new QPushButton(Form);
        cancelarBtn->setObjectName(QString::fromUtf8("cancelarBtn"));
        cancelarBtn->setGeometry(QRect(120, 280, 75, 23));

        retranslateUi(Form);
        QObject::connect(aceptarBtn, SIGNAL(clicked()), Form, SLOT(agregarCurso()));
        QObject::connect(cancelarBtn, SIGNAL(clicked()), Form, SLOT(cancelar()));

        QMetaObject::connectSlotsByName(Form);
    } // setupUi

    void retranslateUi(QWidget *Form)
    {
        Form->setWindowTitle(QApplication::translate("Form", "Form", 0, QApplication::UnicodeUTF8));
        nombreLbl->setText(QApplication::translate("Form", "Nombre:", 0, QApplication::UnicodeUTF8));
        coloniaLbl->setText(QApplication::translate("Form", "Colonia:", 0, QApplication::UnicodeUTF8));
        areaLbl->setText(QApplication::translate("Form", "Area:", 0, QApplication::UnicodeUTF8));
        fechaInicioLbl->setText(QApplication::translate("Form", "Fecha inicio:", 0, QApplication::UnicodeUTF8));
        fechaFinLbl->setText(QApplication::translate("Form", "Fecha fin:", 0, QApplication::UnicodeUTF8));
        enfoqueLbl->setText(QApplication::translate("Form", "Enfoque:", 0, QApplication::UnicodeUTF8));
        aceptarBtn->setText(QApplication::translate("Form", "Aceptar", 0, QApplication::UnicodeUTF8));
        cancelarBtn->setText(QApplication::translate("Form", "Cancelar", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class Form: public Ui_Form {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_AGREGARCURSO_H
