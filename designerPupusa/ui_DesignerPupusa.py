# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DesignerPupusaiHIATP.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import imagenes_rc

class Ui_PupuseriaJuanPerez(object):
    def setupUi(self, PupuseriaJuanPerez):
        if PupuseriaJuanPerez.objectName():
            PupuseriaJuanPerez.setObjectName(u"PupuseriaJuanPerez")
        PupuseriaJuanPerez.resize(466, 610)
        PupuseriaJuanPerez.setStyleSheet(u"background-color: rgb(170, 0, 255);")
        self.centralwidget = QWidget(PupuseriaJuanPerez)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lblEmpresa = QLabel(self.centralwidget)
        self.lblEmpresa.setObjectName(u"lblEmpresa")
        self.lblEmpresa.setGeometry(QRect(0, 0, 471, 81))
        self.lblEmpresa.setMinimumSize(QSize(471, 0))
        font = QFont()
        font.setFamily(u"Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.lblEmpresa.setFont(font)
        self.lblEmpresa.setAutoFillBackground(False)
        self.lblEmpresa.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"font: 63 16pt \"Yu Gothic UI Semibold\";\n"
"")
        self.lblEmpresa.setTextFormat(Qt.RichText)
        self.lblEmpresa.setAlignment(Qt.AlignCenter)
        self.lblEmpresa.setMargin(0)
        self.lblDecorativo = QLabel(self.centralwidget)
        self.lblDecorativo.setObjectName(u"lblDecorativo")
        self.lblDecorativo.setGeometry(QRect(0, 80, 471, 16))
        self.lblDecorativo.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.tdPupusa = QComboBox(self.centralwidget)
        self.tdPupusa.addItem("")
        self.tdPupusa.addItem("")
        self.tdPupusa.addItem("")
        self.tdPupusa.addItem("")
        self.tdPupusa.addItem("")
        self.tdPupusa.addItem("")
        self.tdPupusa.addItem("")
        self.tdPupusa.setObjectName(u"tdPupusa")
        self.tdPupusa.setGeometry(QRect(180, 111, 151, 31))
        self.tdPupusa.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(255, 0, 0);")
        self.lblDequees = QLabel(self.centralwidget)
        self.lblDequees.setObjectName(u"lblDequees")
        self.lblDequees.setGeometry(QRect(40, 110, 131, 31))
        self.lblDequees.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 75 8pt \"MS Sans Serif\";\n"
"border-color: rgb(255, 0, 0);")
        self.lblBebida = QLabel(self.centralwidget)
        self.lblBebida.setObjectName(u"lblBebida")
        self.lblBebida.setGeometry(QRect(40, 180, 131, 31))
        self.lblBebida.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 75 8pt \"MS Sans Serif\";\n"
"border-color: rgb(255, 0, 0);")
        self.TdBebida = QComboBox(self.centralwidget)
        self.TdBebida.addItem("")
        self.TdBebida.addItem("")
        self.TdBebida.addItem("")
        self.TdBebida.addItem("")
        self.TdBebida.addItem("")
        self.TdBebida.setObjectName(u"TdBebida")
        self.TdBebida.setGeometry(QRect(180, 180, 151, 31))
        self.TdBebida.setStyleSheet(u"background-color: rgb(170, 255, 127);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"border-top-color: rgb(255, 0, 0);")
        self.txtDireccionC = QLineEdit(self.centralwidget)
        self.txtDireccionC.setObjectName(u"txtDireccionC")
        self.txtDireccionC.setGeometry(QRect(200, 260, 231, 31))
        self.txtDireccionC.setStyleSheet(u"background-color: rgb(170, 255, 127);")
        self.pagaCon = QLineEdit(self.centralwidget)
        self.pagaCon.setObjectName(u"pagaCon")
        self.pagaCon.setGeometry(QRect(200, 360, 231, 31))
        self.pagaCon.setStyleSheet(u"background-color: rgb(170, 255, 127);")
        self.lblDecorativo_2 = QLabel(self.centralwidget)
        self.lblDecorativo_2.setObjectName(u"lblDecorativo_2")
        self.lblDecorativo_2.setGeometry(QRect(0, 220, 471, 16))
        self.lblDecorativo_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.EnviarCorreo = QPushButton(self.centralwidget)
        self.EnviarCorreo.setObjectName(u"EnviarCorreo")
        self.EnviarCorreo.setGeometry(QRect(110, 450, 161, 23))
        self.EnviarCorreo.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        self.lblDirecCliente = QLabel(self.centralwidget)
        self.lblDirecCliente.setObjectName(u"lblDirecCliente")
        self.lblDirecCliente.setGeometry(QRect(40, 260, 151, 31))
        self.lblDirecCliente.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lblDirecCliente.setAlignment(Qt.AlignCenter)
        self.lblcuenta = QLabel(self.centralwidget)
        self.lblcuenta.setObjectName(u"lblcuenta")
        self.lblcuenta.setGeometry(QRect(40, 310, 151, 31))
        self.lblcuenta.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lblcuenta.setAlignment(Qt.AlignCenter)
        self.lblPagaCon = QLabel(self.centralwidget)
        self.lblPagaCon.setObjectName(u"lblPagaCon")
        self.lblPagaCon.setGeometry(QRect(40, 360, 151, 31))
        self.lblPagaCon.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lblPagaCon.setAlignment(Qt.AlignCenter)
        self.lblTota = QLabel(self.centralwidget)
        self.lblTota.setObjectName(u"lblTota")
        self.lblTota.setGeometry(QRect(40, 410, 151, 31))
        self.lblTota.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lblTota.setAlignment(Qt.AlignCenter)
        self.txtTotal = QLineEdit(self.centralwidget)
        self.txtTotal.setObjectName(u"txtTotal")
        self.txtTotal.setGeometry(QRect(200, 410, 231, 31))
        self.txtTotal.setStyleSheet(u"background-color: rgb(170, 255, 127);")
        self.Grax = QLabel(self.centralwidget)
        self.Grax.setObjectName(u"Grax")
        self.Grax.setGeometry(QRect(300, 520, 151, 31))
        self.Grax.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 75 8pt \"MS Sans Serif\";\n"
"border-color: rgb(255, 0, 0);")
        self.Grax.setAlignment(Qt.AlignCenter)
        self.imagen = QLabel(self.centralwidget)
        self.imagen.setObjectName(u"imagen")
        self.imagen.setGeometry(QRect(360, 102, 81, 111))
        self.imagen.setStyleSheet(u"image: url(:/imagenes.qrc/pupusas.jpg);")
        self.cuenta = QLabel(self.centralwidget)
        self.cuenta.setObjectName(u"cuenta")
        self.cuenta.setGeometry(QRect(200, 310, 231, 31))
        self.cuenta.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        PupuseriaJuanPerez.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(PupuseriaJuanPerez)
        self.statusbar.setObjectName(u"statusbar")
        PupuseriaJuanPerez.setStatusBar(self.statusbar)

        self.retranslateUi(PupuseriaJuanPerez)

        QMetaObject.connectSlotsByName(PupuseriaJuanPerez)
    # setupUi

    def retranslateUi(self, PupuseriaJuanPerez):
        PupuseriaJuanPerez.setWindowTitle(QCoreApplication.translate("PupuseriaJuanPerez", u"MainWindow", None))
        self.lblEmpresa.setText(QCoreApplication.translate("PupuseriaJuanPerez", u"Pupuseria JuanPerez", None))
        self.lblDecorativo.setText("")
        self.tdPupusa.setItemText(0, QCoreApplication.translate("PupuseriaJuanPerez", u"Frijol $0.35", None))
        self.tdPupusa.setItemText(1, QCoreApplication.translate("PupuseriaJuanPerez", u"Queso $0.35", None))
        self.tdPupusa.setItemText(2, QCoreApplication.translate("PupuseriaJuanPerez", u"Revueltas $0.35", None))
        self.tdPupusa.setItemText(3, QCoreApplication.translate("PupuseriaJuanPerez", u"Loroco $0.35", None))
        self.tdPupusa.setItemText(4, QCoreApplication.translate("PupuseriaJuanPerez", u"Ajo $0.40", None))
        self.tdPupusa.setItemText(5, QCoreApplication.translate("PupuseriaJuanPerez", u"Carne $0.40", None))
        self.tdPupusa.setItemText(6, QCoreApplication.translate("PupuseriaJuanPerez", u"Loca $0.65", None))

        self.lblDequees.setText(QCoreApplication.translate("PupuseriaJuanPerez", u"De que es la Pupusa", None))
        self.lblBebida.setText(QCoreApplication.translate("PupuseriaJuanPerez", u"Bebida", None))
        self.TdBebida.setItemText(0, QCoreApplication.translate("PupuseriaJuanPerez", u"Nada $0.00", None))
        self.TdBebida.setItemText(1, QCoreApplication.translate("PupuseriaJuanPerez", u"Bolsa con agua $0.25", None))
        self.TdBebida.setItemText(2, QCoreApplication.translate("PupuseriaJuanPerez", u"Jugo $0.50", None))
        self.TdBebida.setItemText(3, QCoreApplication.translate("PupuseriaJuanPerez", u"Fresco $0.50", None))
        self.TdBebida.setItemText(4, QCoreApplication.translate("PupuseriaJuanPerez", u"Soda $0.75", None))

        self.lblDecorativo_2.setText("")
        self.EnviarCorreo.setText(QCoreApplication.translate("PupuseriaJuanPerez", u"Enviar Recibo", None))
        self.lblDirecCliente.setText(QCoreApplication.translate("PupuseriaJuanPerez", u"Dirreccion de correo cliente", None))
        self.lblcuenta.setText(QCoreApplication.translate("PupuseriaJuanPerez", u"Cuenta: ", None))
        self.lblPagaCon.setText(QCoreApplication.translate("PupuseriaJuanPerez", u"Paga con: ", None))
        self.lblTota.setText(QCoreApplication.translate("PupuseriaJuanPerez", u"Total: ", None))
        self.Grax.setText(QCoreApplication.translate("PupuseriaJuanPerez", u"Gracias por Preferirnos", None))
        self.imagen.setText("")
        self.cuenta.setText("")
    # retranslateUi

