# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_datos.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize
from PySide6.QtWidgets import QFormLayout, QLabel, QPushButton


class Ui_w_datos(object):
    def setupUi(self, w_datos):
        if not w_datos.objectName():
            w_datos.setObjectName("w_datos")
        w_datos.resize(510, 374)
        w_datos.setMinimumSize(QSize(510, 374))
        w_datos.setMaximumSize(QSize(510, 374))
        w_datos.setStyleSheet(
            "QWidget#Form {\n"
            "    background-color: #f9f9f9;\n"
            "    padding: 16px;\n"
            "    border-radius: 4px;\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    font-weight: 500;\n"
            "    color: #202124;\n"
            "    margin-bottom: 8px;\n"
            "   \n"
            "}\n"
            "\n"
            "QPushButton {\n"
            "    background-color: #1a73e8;\n"
            "    color: white;\n"
            "    border: none;\n"
            "    padding: 10px 24px;\n"
            "    border-radius: 4px;\n"
            "    font-size: 14px;\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton{ \n"
            "    background-color: #dc3545; \n"
            "    color: white;\n"
            "    border: none;\n"
            "    padding: 10px 24px;\n"
            "    border-radius: 4px;\n"
            "    font-size: 14px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #c82333; \n"
            "}\n"
            "\n"
            ""
        )
        self.formLayout = QFormLayout(w_datos)
        self.formLayout.setObjectName("formLayout")
        self.label = QLabel(w_datos)
        self.label.setObjectName("label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.label_2 = QLabel(w_datos)
        self.label_2.setObjectName("label_2")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.label_3 = QLabel(w_datos)
        self.label_3.setObjectName("label_3")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.SpanningRole, self.label_3)

        self.label_4 = QLabel(w_datos)
        self.label_4.setObjectName("label_4")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.SpanningRole, self.label_4)

        self.pushButton = QPushButton(w_datos)
        self.pushButton.setObjectName("pushButton")

        self.formLayout.setWidget(12, QFormLayout.ItemRole.FieldRole, self.pushButton)

        self.label_correo = QLabel(w_datos)
        self.label_correo.setObjectName("label_correo")
        self.label_correo.setStyleSheet(
            "QLabel {\n" "    font-style: italic; \n" "    color: #6c757d; \n" "}"
        )

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_correo)

        self.label_nombre = QLabel(w_datos)
        self.label_nombre.setObjectName("label_nombre")
        self.label_nombre.setStyleSheet(
            "QLabel {\n"
            "    font-weight: normal; /* No negrita */\n"
            "    color: #007bff; /* Color azul */\n"
            "    font-size: 1.2em; /* Un poco m\u00e1s grande */\n"
            "}"
        )

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_nombre)

        self.label_fecha_actual = QLabel(w_datos)
        self.label_fecha_actual.setObjectName("label_fecha_actual")
        self.label_fecha_actual.setStyleSheet("QLabel {\n" "    color: #28a745; \n" "}")

        self.formLayout.setWidget(
            7, QFormLayout.ItemRole.LabelRole, self.label_fecha_actual
        )

        self.label_ultima = QLabel(w_datos)
        self.label_ultima.setObjectName("label_ultima")
        self.label_ultima.setStyleSheet("QLabel {\n" "    color: #dc3545; \n" "}\n" "")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.LabelRole, self.label_ultima)

        self.retranslateUi(w_datos)

        QMetaObject.connectSlotsByName(w_datos)

    # setupUi

    def retranslateUi(self, w_datos):
        w_datos.setWindowTitle(QCoreApplication.translate("w_datos", "datos", None))
        self.label.setText(QCoreApplication.translate("w_datos", "Nombre:", None))
        self.label_2.setText(QCoreApplication.translate("w_datos", "Correo:", None))
        self.label_3.setText(
            QCoreApplication.translate("w_datos", "Fecha actual:", None)
        )
        self.label_4.setText(
            QCoreApplication.translate("w_datos", "\u00faltima conexi\u00f3n", None)
        )
        self.pushButton.setText(QCoreApplication.translate("w_datos", "salir", None))
        self.label_correo.setText(
            QCoreApplication.translate("w_datos", "alvaro@alvaro.com", None)
        )
        self.label_nombre.setText(QCoreApplication.translate("w_datos", "Alvaro", None))
        self.label_fecha_actual.setText(
            QCoreApplication.translate("w_datos", "fecha", None)
        )
        self.label_ultima.setText(QCoreApplication.translate("w_datos", "fecha", None))

    # retranslateUi
