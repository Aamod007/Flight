# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Nistara_Cancellation_Info.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1201, 801)
        self.HeaderLabel = QLabel(Dialog)
        self.HeaderLabel.setObjectName(u"HeaderLabel")
        self.HeaderLabel.setGeometry(QRect(210, 30, 771, 71))
        self.HeaderLabel.setStyleSheet(u"\n"
"font: 36pt \"MS Shell Dlg 2\";")
        self.HeaderLabel.setAlignment(Qt.AlignCenter)
        self.Payments_Info_TableWidget = QTableWidget(Dialog)
        if (self.Payments_Info_TableWidget.columnCount() < 5):
            self.Payments_Info_TableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.Payments_Info_TableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.Payments_Info_TableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.Payments_Info_TableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.Payments_Info_TableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.Payments_Info_TableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.Payments_Info_TableWidget.setObjectName(u"Payments_Info_TableWidget")
        self.Payments_Info_TableWidget.setGeometry(QRect(30, 190, 1151, 431))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(310, 130, 551, 31))
        self.label.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.label.setAlignment(Qt.AlignCenter)
        self.Back_Button = QPushButton(Dialog)
        self.Back_Button.setObjectName(u"Back_Button")
        self.Back_Button.setGeometry(QRect(470, 700, 281, 51))
        self.Back_Button.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.HeaderLabel.setText(QCoreApplication.translate("Dialog", u"Nistara Cancellation Info", None))
        ___qtablewidgetitem = self.Payments_Info_TableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Cancellation ID", None));
        ___qtablewidgetitem1 = self.Payments_Info_TableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Cancellation Payment ID", None));
        ___qtablewidgetitem2 = self.Payments_Info_TableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Cancellation Refund", None));
        ___qtablewidgetitem3 = self.Payments_Info_TableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Cancellation Date", None));
        ___qtablewidgetitem4 = self.Payments_Info_TableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"Flight Company", None));
        self.label.setText("")
        self.Back_Button.setText(QCoreApplication.translate("Dialog", u"Back", None))
    # retranslateUi

