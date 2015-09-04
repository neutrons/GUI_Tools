#
# N(DAV)TableWidget
#

from PyQt4 import QtGui, QtCore

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class NTableWidget(QtGui.QTableWidget):
    """
    NdavTableWidget inherits from QTableWidget
    """
    def __init__(self, parent):
        """

        :param parent:
        :return:
        """
        QtGui.QTableWidget.__init__(self, parent)

        self._myParent = parent

        return

    def append_row(self, row_value_list, type_list):
        """

        :param row_value_list:
        :return:
        """
        # Check input
        assert isinstance(row_value_list, list)
        assert isinstance(type_list, list)
        assert len(row_value_list) == len(type_list)
        if len(row_value_list) != self.columnCount():
            ret_msg = 'Input number of values (%d) is different from column number (%d).' % (len(row_value_list),
                                                                                             self.columnCount())
        else:
            ret_msg = ''

        # Insert new row
        row_number = self.rowCount()
        self.insertRow(row_number)

        # Set values
        for i_col in xrange(min(len(row_value_list), self.columnCount())):
            item = QtGui.QTableWidgetItem()
            item.setText(_fromUtf8(row_value_list[i_col]))
            item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
            if type_list[i_col] == 'checkbox':
                self.set_check_box(row_number, i_col, False)
            else:
                self.setItem(row_number, i_col, item)
        # END-FOR(i_col)

        return ret_msg

    def init_setup(self, column_tup_list):
        """ Initial setup
        :param column_tup_list: list of 2-tuple as string (column name) and string (data type)
        :return:
        """
        # Define column headings
        num_cols = len(column_tup_list)

        table_head_list = list()
        for c_tup in column_tup_list:
            c_name = c_tup[0]
            table_head_list.append(c_name)

        self.setColumnCount(num_cols)
        self.setHorizontalHeaderLabels(table_head_list)

        return

    def set_check_box(self, row, col, state):
        """ function to add a new select checkbox to a cell in a table row
        won't add a new checkbox if one already exists
        """
        # Check input
        assert isinstance(state, bool)

        # Check if cellWidget exists
        if self.cellWidget(row,col):
            # existing: just set the value
            self.cellWidget(row, col).setChecked(state)
        else:
            # case to add checkbox
            checkbox = QtGui.QCheckBox()
            checkbox.setText('')
            checkbox.setChecked(state)

            # Adding a widget which will be inserted into the table cell
            # then centering the checkbox within this widget which in turn,
            # centers it within the table column :-)
            self.setCellWidget(row, col, checkbox)
        # END-IF-ELSE

        return
