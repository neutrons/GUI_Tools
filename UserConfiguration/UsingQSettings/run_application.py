from interface_example import Ui_MainWindow
from PyQt4 import QtGui, QtCore
import sys


class MyApplication(QtGui.QMainWindow):
    
    _save_directory = None
    
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        settings = QtCore.QSettings()
        self._save_directory = settings.value("saved_text", '')

    def save_settings(self):
        text = self.ui.textEdit.toPlainText()
        settings = QtCore.QSettings()
        settings.setValue("saved_text", text)
        
    def load_settings(self):
        settings = QtCore.QSettings()
        self.ui.textEdit.setText(settings.value("saved_text"))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mplQt = MyApplication()
    mplQt.show()
    sys.exit(app.exec_())