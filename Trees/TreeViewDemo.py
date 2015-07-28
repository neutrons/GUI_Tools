#
# Features:
# 1. Add items to tree view
# 2. Select multiple items of tree view
# 3. Enabled right-click menu of the selected items
# 4. Drag and drop 
#
# Success:
# 2. Select multiple items of tree view
# 3. Enable right-click menu 
#
# Failed:
# 4. Enable drag from treeview/model/item to plain text
#

import sys

from PyQt4 import QtGui, QtCore, Qt

import TreeViewExperiment as mainUi

class TreeViewWindow(QtGui.QMainWindow):
    """ Main GUI class for VDrive of the beta version
    """

    # initialize app
    def __init__(self, parent=None):
        """ Init
        """
        # Setup main window
        QtGui.QMainWindow.__init__(self, parent)
        self.setWindowTitle('TreeView Demo')
        self.ui = mainUi.Ui_MainWindow()
        self.ui.setupUi(self)

        actionpairlist = [ 
                ('Add', self.doAddFile),
                ('Info', self.doPrintInfo)]

        self._setupStandardTreeView(self.ui.treeView_main, actionpairlist)
        self._setupFileSystemTreeView(self.ui.treeView_file)

        # Event handling
        self.connect(self.ui.pushButton_addCol0, QtCore.SIGNAL('clicked()'),
                self.do_add_item_to_col0)
        self.connect(self.ui.pushButton_appendCol0, QtCore.SIGNAL('clicked()'),
                self.do_append_item_to_col0)
        self.connect(self.ui.pushButton_appendCol1, QtCore.SIGNAL('clicked()'),
                self.do_append_item_to_col1)

        # Drag and drop setup
        self.ui.lineEdit_col0.setDragEnabled(True)
        self.ui.plainTextEdit_main.setAcceptDrops(True)

        return


    #-------------------------------------------------------------------------
    # Example to set up a TreeView widget
    #-------------------------------------------------------------------------
    def _setupStandardTreeView(self, treeviewwidget, actionpairlist):
        """ Set up tree view including 
        (1) model
        (2) action menu
        """
        # Tree widget setup for multiple selection
        treeviewwidget.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)

        # Model with 2 columns
        model = QtGui.QStandardItemModel()
        model.setColumnCount(2)
        # model.setDragEnabled(True) Not allowed

        # Header
        model.setHeaderData(0, QtCore.Qt.Horizontal, 'IPTS')
        model.setHeaderData(1, QtCore.Qt.Horizontal, 'Run')
        # Set model and column width
        treeviewwidget.setModel(model)
        treeviewwidget.setColumnWidth(0, 90)
        treeviewwidget.setColumnWidth(1, 60)

        treeviewwidget.setDragEnabled(True)

        # Add action menu: to use right mouse operation for pop-up sub menu 
        for actionname, method in actionpairlist:
            action = QtGui.QAction(actionname, self)
            action.triggered.connect(method)
            treeviewwidget.addAction(action)
        treeviewwidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)

        return


    def _setupFileSystemTreeView(self, treeviewwidget):
        """ Set up a TreeView with file browser
        """
        import os
        curdir = os.getcwd()

        # Tree widget setup
        treeviewwidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)

        # Model
        filemodel = QtGui.QFileSystemModel()
        curpath = QtCore.QString(curdir)
        filemodel.setRootPath( '/home/wzz' )

        # Set model
        treeviewwidget.setModel(filemodel)

        # Set the root path (no parent)
        idx = treeviewwidget.model().index('/home/wzz')
        treeviewwidget.setRootIndex(idx)

        # Set the default path (current view)
        idx = treeviewwidget.model().index('/home/wzz/Mantid_Project/GUI_Tools/')
        treeviewwidget.setCurrentIndex(idx)

        # Link
        self.connect(treeviewwidget, QtCore.SIGNAL('clicked()'),
                self.do_click_file_system)

        # Action list
        actionpairlist = [('Info', self.doPrintFileTreeInfo)]

        for actionname, method in actionpairlist:
            action = QtGui.QAction(actionname, self)
            action.triggered.connect(method)
            treeviewwidget.addAction(action)
        treeviewwidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)

    #-------------------------------------------------------------------------
    # End of Example to set up a TreeView widget
    #-------------------------------------------------------------------------

    def doAddFile(self):
        """
        """
        print "Add file"


    def doPrintFileTreeInfo(self):
        """ 
        """
        indexes = self.ui.treeView_file.selectedIndexes()
        print "Number of indexes = ", len(indexes)
        for index in indexes:
            print "Row = ", index.row(), "Col = ", index.column(), ": ",
            #item = self.ui.treeView_file.model().item(index.row(), index.column()): no method item()
            filename = self.ui.treeView_file.model().fileName(index)
            print filename, type(filename)
            

        return

    def doPrintInfo(self):
        """
        """
        # Get selected indexes of the tree
        # NOTE: indexes will be all items of the row(s) that are selected: such as (0, 0), (0, 1), (3, 0), (3, 1)
        indexes = self.ui.treeView_main.selectedIndexes()
        print "Number of selected indexes = %d." % (len(indexes))
        for index in indexes:
            item = self.ui.treeView_main.model().item(index.row(), index.column())
            print index, index.row(), index.column(), ": ", 
            if item is None:
                print "<None>", 
            else:
                print str(item.text()), 
            print self.ui.treeView_main.model().itemData(index)


    def do_click_file_system(self):
        """
        """
        print "Clicked File System."

    def do_add_item_to_col0(self):
        """ Add an item in line edit to column 0 by current index
        """
        value = str(self.ui.lineEdit_col0.text())

        # Get selected indexes of the tree
        indexes = self.ui.treeView_main.selectedIndexes()
        if len(indexes) == 0:
            # non-selected: appending     
            numrows = self.ui.treeView_main.model().rowCount()
            print "Current treeview has %d rows."%(numrows)

            # new item
            itemmain = QtGui.QStandardItem(QtCore.QString(value)) 
            itemmain.setCheckable(False)
            itemmain.setDragEnabled(True)
            inewrow = numrows
            self.ui.treeView_main.model().setItem(inewrow, 0, itemmain)

        else:
            # with select item: insert a row?
            raise NotImplementedError('Next step!')


    def do_append_item_to_col0(self):
        """ Append... copy code from do_add_item_col0
        """
        value = str(self.ui.lineEdit_col0.text())

        # non-selected: appending     
        numrows = self.ui.treeView_main.model().rowCount()
        print "Current treeview has %d rows."%(numrows)

        # new item
        itemmain = QtGui.QStandardItem(QtCore.QString(value)) 
        itemmain.setCheckable(False)
        inewrow = numrows
        self.ui.treeView_main.model().setItem(inewrow, 0, itemmain)

        return

    def do_append_item_to_col1(self):
        """ Append... copy code from do_add_item_col0
        """
        iCol = 1

        value = str(self.ui.lineEdit_col1.text())

        # non-selected: appending     
        numrows = self.ui.treeView_main.model().rowCount()
        print "Current treeview has %d rows."%(numrows)

        # new item
        itemmain = QtGui.QStandardItem(QtCore.QString(value)) 
        itemmain.setCheckable(False)
        inewrow = numrows
        self.ui.treeView_main.model().setItem(inewrow, iCol, itemmain)

        return



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = TreeViewWindow()
    myapp.show()

    exit_code=app.exec_()
    sys.exit(exit_code)
