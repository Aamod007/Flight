from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel
import sys

class WelcomeScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        uic.loadUi(r"Project_Source_Code/Welcome_UI_Screen.ui", self)
        
        # Background animation setup
        self.bgwidget = self.findChild(QtWidgets.QWidget, "bgwidget")
        self.bg_label = QLabel(self.bgwidget)
        self.bg_label.setGeometry(0, 0, self.bgwidget.width(), self.bgwidget.height())
        
        self.movie = QMovie("Project_Source_Code/background.gif")
        self.bg_label.setMovie(self.movie)
        self.movie.start()
        
        # Button connections
        self.Customer = self.findChild(QtWidgets.QPushButton, "Customer")
        self.Admin = self.findChild(QtWidgets.QPushButton, "Admin")
        
        self.Customer.clicked.connect(self.gotoCustomer)
        self.Admin.clicked.connect(self.gotoAdmin)

    def gotoCustomer(self):
        print("Navigating to Customer Screen...")
        # Add navigation logic here

    def gotoAdmin(self):
        print("Navigating to Admin Screen...")
        # Add navigation logic here

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WelcomeScreen()
    window.show()
    sys.exit(app.exec_())
