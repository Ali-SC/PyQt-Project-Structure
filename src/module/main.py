import sys
import ui.frmMain as main_form
from PyQt5.QtWidgets import QMainWindow, QApplication

class MyAppName(QMainWindow, main_form.Ui_frmMain):
    def __init__(self, parent=None):
        super(MyAppName, self).__init__(parent)
        self.setupUi(self)

        #self.ui.btnCal_Done.clicked.connect(self.Save_and_Close)

        #self.btnAbout.clicked.connect(self.Show_About)
        #self.btnCalibrateSpectrometerLink.clicked.connect(self.openWindow)
        self.show()


def refresh():
    QApplication.processEvents()


def main():
    app = QApplication(sys.argv)
    form = MyAppName()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()