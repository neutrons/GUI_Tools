#!/usr/bin/python
#
# Main script to demo table
#
import sys
from PyQt4 import QtGui, QtCore

# include this try/except block to remap QString needed when using IPython
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

# import GUI components generated from Qt Designer .ui file
import ui_DemoTable

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class DemoTableWindow(QtGui.QMainWindow):
    """
    Class to
    """
    def __init__(self, parent=None):
        """
        Init
        :param parent:
        :return:
        """
        # setup main window
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = ui_DemoTable.Ui_MainWindow()
        self.ui.setupUi(self)

        # Event handling
        self.connect(self.ui.actionExit, QtCore.SIGNAL('triggered()'),
                     self.do_quit)

        # Buttons
        self.connect(self.ui.pushButton_initSetup, QtCore.SIGNAL('clicked()'),
                     self.do_init_table)

        self.connect(self.ui.pushButton_setDefault, QtCore.SIGNAL('clicked()'),
                     self.do_set_default)

        self.connect(self.ui.pushButton_appendRow, QtCore.SIGNAL('clicked()'),
                     self.do_append_row)

        self._columnTypeList = list()

        return

    def do_append_row(self):
        """

        :return:
        """
        input_str = str(self.ui.lineEdit_newRow.text())
        terms = input_str.strip().split(';')
        row_value_list = list()
        for term in terms:
            row_value_list.append(term.strip())

        type_list = self._columnTypeList

        self.ui.tableWidget_main.append_row(row_value_list, type_list)

        return

    def do_init_table(self):
        """
        Init table
        :return:
        """
        user_column_str = str(self.ui.lineEdit_tableColumns.text())

        # Interpret
        column_str_list = user_column_str.split(';')
        column_tup_list = list()
        for column_str in column_str_list:
            terms = column_str.strip().split(',')
            col_name = terms[0].strip()
            col_type = terms[1].strip()
            column_tup_list.append((col_name, col_type))
            self._columnTypeList.append(col_type)

        self.ui.tableWidget_main.init_setup(column_tup_list)

        return

    def do_set_default(self):
        """

        :return:
        """
        default_str = 'Scan, int; Pt, int; H, float; K, float; L, float; Q_x, float; Q_y, float; Q_z, float; ' \
                      'Status, checkbox'
        self.ui.lineEdit_tableColumns.setText(default_str)

        return

    def do_quit(self):
        """
        Quit
        :return:
        """
        self.close()

        return


# Main program
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    my_app = DemoTableWindow()
    my_app.show()

    exit_code = app.exec_()
    sys.exit(exit_code)
