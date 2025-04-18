# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QWidget)

class Ui_ui_main(object):
    def setupUi(self, ui_main):
        if not ui_main.objectName():
            ui_main.setObjectName(u"ui_main")
        ui_main.resize(874, 551)
        ui_main.setStyleSheet(u"QWidget {\n"
"    background-color: #f8f9fa;\n"
"    font-family: \"Roboto\", \"Segoe UI\", \"Helvetica Neue\", sans-serif;\n"
"    font-size: 14px;\n"
"    color: #202124;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #fff;\n"
"    color: #202124;\n"
"    border: 1px solid #dadce0;\n"
"    border-radius: 4px;\n"
"    padding: 10px 16px;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"    margin-bottom: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #e8f0fe;\n"
"    border-color: #e8f0fe;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #dbe9fd;\n"
"    border-color: #dbe9fd;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"    border-color: #1a73e8;\n"
"}\n"
" \n"
"")
        self.gridLayout_2 = QGridLayout(ui_main)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabla_Alumno = QTableView(ui_main)
        self.tabla_Alumno.setObjectName(u"tabla_Alumno")

        self.gridLayout_2.addWidget(self.tabla_Alumno, 0, 0, 1, 1)

        self.frame = QFrame(ui_main)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.button_eliminar = QPushButton(self.frame)
        self.button_eliminar.setObjectName(u"button_eliminar")
        self.button_eliminar.setStyleSheet(u"QPushButton {\n"
"    background-color: #ff9800; \n"
"    color: #fff;\n"
"    border-color: #ff9800;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f57c00;\n"
"    border-color: #f57c00;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #e65100;\n"
"    border-color: #e65100;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"    border-color: #ff9800;\n"
"}")

        self.gridLayout.addWidget(self.button_eliminar, 0, 0, 1, 1)

        self.button_cargar = QPushButton(self.frame)
        self.button_cargar.setObjectName(u"button_cargar")
        self.button_cargar.setStyleSheet(u"QPushButton{\n"
"    background-color: #1a73e8; \n"
"    color: #fff;\n"
"    border-color: #1a73e8;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3c83f1;\n"
"    border-color: #3c83f1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #185abc;\n"
"    border-color: #185abc;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"    border-color: #1a73e8;\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout.addWidget(self.button_cargar, 1, 0, 1, 1)

        self.butto_mostrar = QPushButton(self.frame)
        self.butto_mostrar.setObjectName(u"butto_mostrar")
        self.butto_mostrar.setStyleSheet(u"QPushButton{\n"
"    background-color: #4caf50; \n"
"    color: #fff;\n"
"    border-color: #4caf50;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #43a047;\n"
"    border-color: #43a047;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #388e3c;\n"
"    border-color: #388e3c;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"    border-color: #4caf50;\n"
"}")

        self.gridLayout.addWidget(self.butto_mostrar, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 286, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.button_salir = QPushButton(self.frame)
        self.button_salir.setObjectName(u"button_salir")
        self.button_salir.setStyleSheet(u"\n"
"QPushButton{\n"
"    background-color: #f44336; \n"
"    color: #fff;\n"
"    border-color: #f44336;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #e53935;\n"
"    border-color: #e53935;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #d32f2f;\n"
"    border-color: #d32f2f;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"    border-color: #f44336;\n"
"}")

        self.gridLayout.addWidget(self.button_salir, 4, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 1, 1, 1)


        self.retranslateUi(ui_main)

        QMetaObject.connectSlotsByName(ui_main)
    # setupUi

    def retranslateUi(self, ui_main):
        ui_main.setWindowTitle(QCoreApplication.translate("ui_main", u"Datos", None))
        self.button_eliminar.setText(QCoreApplication.translate("ui_main", u"Eliminar Tabla", None))
        self.button_cargar.setText(QCoreApplication.translate("ui_main", u"Cargar archivo", None))
        self.butto_mostrar.setText(QCoreApplication.translate("ui_main", u"Mostrar alumno", None))
        self.button_salir.setText(QCoreApplication.translate("ui_main", u"Salir", None))
    # retranslateUi

