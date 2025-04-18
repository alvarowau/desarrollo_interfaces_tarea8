# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_conection.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_ui_conection(object):
    def setupUi(self, ui_conection):
        if not ui_conection.objectName():
            ui_conection.setObjectName(u"ui_conection")
        ui_conection.resize(321, 451)
        ui_conection.setMinimumSize(QSize(321, 451))
        ui_conection.setMaximumSize(QSize(321, 451))
        ui_conection.setStyleSheet(u"\n"
"QWidget {\n"
"    background-color: #f8f9fa; \n"
"    font-family: \"Roboto\", \"Segoe UI\", \"Helvetica Neue\", sans-serif;\n"
"    font-size: 14px;\n"
"    color: #202124; \n"
"}\n"
"\n"
"QLabel {\n"
"    color: #5f6368; \n"
"    margin-bottom: 8px; \n"
"    font-weight: normal; \n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #fff;\n"
"    border: 1px solid #dadce0;\n"
"    border-radius: 4px;\n"
"    padding: 8px; \n"
"    margin-bottom: 15px;\n"
"    font-size: 16px;\n"
"    selection-background-color: #1a73e8;\n"
"    selection-color: #fff;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    outline: none;\n"
"    border-color: #1a73e8;  \n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #1a73e8;\n"
"    color: #fff;\n"
"    border: none;\n"
"    border-radius: 4px;\n"
"    padding: 8px 16px;\n"
"    font-size: 14px; \n"
"    font-weight: bold;\n"
"    qproperty-default: false; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3c83f1; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    backgro"
                        "und-color: #185abc;\n"
"}\n"
"\n"
"QPushButton#conectarButton { \n"
"    padding: 10px 24px; \n"
"    font-size: 16px;\n"
"}")
        self.frame = QFrame(ui_conection)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 321, 451))
        self.frame.setMinimumSize(QSize(321, 451))
        self.frame.setMaximumSize(QSize(321, 451))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_host = QLabel(self.frame)
        self.label_host.setObjectName(u"label_host")

        self.gridLayout.addWidget(self.label_host, 0, 0, 1, 1)

        self.line_host = QLineEdit(self.frame)
        self.line_host.setObjectName(u"line_host")

        self.gridLayout.addWidget(self.line_host, 0, 1, 1, 2)

        self.label_user = QLabel(self.frame)
        self.label_user.setObjectName(u"label_user")

        self.gridLayout.addWidget(self.label_user, 1, 0, 1, 1)

        self.line_user = QLineEdit(self.frame)
        self.line_user.setObjectName(u"line_user")

        self.gridLayout.addWidget(self.line_user, 1, 1, 1, 2)

        self.label_password = QLabel(self.frame)
        self.label_password.setObjectName(u"label_password")

        self.gridLayout.addWidget(self.label_password, 2, 0, 1, 2)

        self.line_password = QLineEdit(self.frame)
        self.line_password.setObjectName(u"line_password")

        self.gridLayout.addWidget(self.line_password, 2, 2, 1, 1)

        self.label_database = QLabel(self.frame)
        self.label_database.setObjectName(u"label_database")

        self.gridLayout.addWidget(self.label_database, 3, 0, 1, 2)

        self.line_database = QLineEdit(self.frame)
        self.line_database.setObjectName(u"line_database")

        self.gridLayout.addWidget(self.line_database, 3, 2, 1, 1)

        self.label_port = QLabel(self.frame)
        self.label_port.setObjectName(u"label_port")

        self.gridLayout.addWidget(self.label_port, 4, 0, 1, 1)

        self.line_port = QLineEdit(self.frame)
        self.line_port.setObjectName(u"line_port")

        self.gridLayout.addWidget(self.line_port, 4, 2, 1, 1)

        self.button_conectar = QPushButton(self.frame)
        self.button_conectar.setObjectName(u"button_conectar")
        self.button_conectar.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.button_conectar, 5, 2, 1, 1)


        self.retranslateUi(ui_conection)

        QMetaObject.connectSlotsByName(ui_conection)
    # setupUi

    def retranslateUi(self, ui_conection):
        ui_conection.setWindowTitle(QCoreApplication.translate("ui_conection", u"Conection", None))
        self.label_host.setText(QCoreApplication.translate("ui_conection", u"Host:", None))
        self.label_user.setText(QCoreApplication.translate("ui_conection", u"User:", None))
        self.label_password.setText(QCoreApplication.translate("ui_conection", u"Password:", None))
        self.label_database.setText(QCoreApplication.translate("ui_conection", u"Data Base:", None))
        self.label_port.setText(QCoreApplication.translate("ui_conection", u"Port:", None))
        self.button_conectar.setText(QCoreApplication.translate("ui_conection", u"Conectar", None))
    # retranslateUi

