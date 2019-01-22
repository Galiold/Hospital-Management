from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
import ui


def btn_clicked(textbox):
    # textbox.setText("Hello")
    print(textbox.toPlainText())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    text = ui.textEdit
    ui.login.clicked.connect(partial(btn_clicked, text))

    sys.exit(app.exec_())
