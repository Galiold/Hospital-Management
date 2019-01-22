from PyQt5.QtWidgets import QTableWidgetItem
# from PyQt5.uic.properties import QtGui


def fill_pending_user_table(pending_list, ui):
    ui.tableWidget.setRowCount(len(pending_list))
    ui.tableWidget.setColumnCount(len(pending_list[0]))
    for i in range(len(pending_list)):
        for j in range(len(pending_list[0])):
            ui.tableWidget.setItem(i, j, QTableWidgetItem(str(pending_list[i][j])))
