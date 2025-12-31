import sys
from PyQt5 import QtWidgets, uic
from core.auth import authenticate
import core.config as config

class LoginWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/login.ui", self)

        self.pushButton.clicked.connect(self.login)

    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        user = authenticate(username, password)

        if user:
            config.current_user = user
            self.status_message.setText("Login Successful")
            self.open_dashboard()
        else:
            self.status_message.setText("Login Unsuccessful")

    def open_dashboard(self):
        self.dashboard = DashboardWindow()
        self.dashboard.show()
        self.close()

class DashboardWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/dashboard.ui", self)
        self.welcome_label.setText(
            f"Welcome {config.current_user[1]}"
        )
def start_gui():
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
