# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Update_Flight_Information.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_bgwidget(object):
    def setupUi(self, bgwidget):
        if not bgwidget.objectName():
            bgwidget.setObjectName(u"bgwidget")
        bgwidget.resize(1201, 801)
        self.label_3 = QLabel(bgwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(250, 150, 191, 21))
        self.label_3.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")
        self.Flight_ID = QLineEdit(bgwidget)
        self.Flight_ID.setObjectName(u"Flight_ID")
        self.Flight_ID.setGeometry(QRect(490, 110, 231, 51))
        self.Flight_ID.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")
        self.Proceed_To_Summary_Button = QPushButton(bgwidget)
        self.Proceed_To_Summary_Button.setObjectName(u"Proceed_To_Summary_Button")
        self.Proceed_To_Summary_Button.setGeometry(QRect(430, 640, 331, 81))
        self.Proceed_To_Summary_Button.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.SUMMARY_Label = QLabel(bgwidget)
        self.SUMMARY_Label.setObjectName(u"SUMMARY_Label")
        self.SUMMARY_Label.setGeometry(QRect(180, 10, 821, 51))
        self.SUMMARY_Label.setStyleSheet(u"\n"
"font: 30pt \"MS Shell Dlg 2\";")
        self.SUMMARY_Label.setAlignment(Qt.AlignCenter)
        self.Error_Popup_Message = QLabel(bgwidget)
        self.Error_Popup_Message.setObjectName(u"Error_Popup_Message")
        self.Error_Popup_Message.setGeometry(QRect(430, 170, 391, 21))
        self.Error_Popup_Message.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.Error_Popup_Message.setAlignment(Qt.AlignCenter)
        self.Enter_Flight_ID_Label = QLabel(bgwidget)
        self.Enter_Flight_ID_Label.setObjectName(u"Enter_Flight_ID_Label")
        self.Enter_Flight_ID_Label.setGeometry(QRect(250, 110, 221, 41))
        self.Enter_Flight_ID_Label.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";")
        self.User_Flight_Details = QTableWidget(bgwidget)
        if (self.User_Flight_Details.columnCount() < 9):
            self.User_Flight_Details.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.User_Flight_Details.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.User_Flight_Details.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.User_Flight_Details.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.User_Flight_Details.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.User_Flight_Details.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.User_Flight_Details.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.User_Flight_Details.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.User_Flight_Details.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.User_Flight_Details.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.User_Flight_Details.setObjectName(u"User_Flight_Details")
        self.User_Flight_Details.setGeometry(QRect(10, 200, 1171, 421))
        self.User_Input_Flight_ID = QPushButton(bgwidget)
        self.User_Input_Flight_ID.setObjectName(u"User_Input_Flight_ID")
        self.User_Input_Flight_ID.setGeometry(QRect(760, 110, 281, 51))
        self.User_Input_Flight_ID.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")

        self.retranslateUi(bgwidget)

        QMetaObject.connectSlotsByName(bgwidget)
    # setupUi

    def retranslateUi(self, bgwidget):
        bgwidget.setWindowTitle(QCoreApplication.translate("bgwidget", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("bgwidget", u"(To proceed to Payment)", None))
        self.Proceed_To_Summary_Button.setText(QCoreApplication.translate("bgwidget", u"UPDATE", None))
        self.SUMMARY_Label.setText(QCoreApplication.translate("bgwidget", u"UPDATE FLIGHT DETAILS", None))
        self.Error_Popup_Message.setText("")
        self.Enter_Flight_ID_Label.setText(QCoreApplication.translate("bgwidget", u"Enter Flight ID :", None))
        ___qtablewidgetitem = self.User_Flight_Details.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("bgwidget", u"Flight ID", None));
        ___qtablewidgetitem1 = self.User_Flight_Details.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("bgwidget", u"Flight Departure", None));
        ___qtablewidgetitem2 = self.User_Flight_Details.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("bgwidget", u"Flight Arrival", None));
        ___qtablewidgetitem3 = self.User_Flight_Details.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("bgwidget", u"Flight Company", None));
        ___qtablewidgetitem4 = self.User_Flight_Details.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("bgwidget", u"Flight Duration", None));
        ___qtablewidgetitem5 = self.User_Flight_Details.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("bgwidget", u"Departure Time", None));
        ___qtablewidgetitem6 = self.User_Flight_Details.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("bgwidget", u"Arrival Time", None));
        ___qtablewidgetitem7 = self.User_Flight_Details.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("bgwidget", u"Seats", None));
        ___qtablewidgetitem8 = self.User_Flight_Details.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("bgwidget", u"Company ID", None));
        self.User_Input_Flight_ID.setText(QCoreApplication.translate("bgwidget", u"Load Details", None))
    # retranslateUi

