import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import login
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QMainWindow()
    ui = login.Ui_MainWindow()
    ui.setupUi(win)
    win.show()
    sys.exit(app.exec_())