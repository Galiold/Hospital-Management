from functools import partial

from PyQt5 import QtWidgets

import login
import ui


def btn_clicked(ui):
    # textbox.setText("Hello")
    username_in = ui.username.toPlainText()
    pass_in = ui.password.toPlainText()
    login.login(username_in, pass_in)
    # print(textbox.toPlainText())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.login_btn.clicked.connect(partial(btn_clicked, ui))

    sys.exit(app.exec_())
