```
1
background-color: rgba(16,30,41,240);
border-radius:10px;

2
background-color: rgba(0, 0, 0,0);
border:1px solid rgba(0,0,0,0);
border-bottom-color:rgba(255,255,255,200);
padding-bottom:7px;

3
QPushButton#pushButton{
background-color:rgba(2,65,118,255);
color:rgba(255,255,255,200);
border-radius:5px;
}
QPushButton#pushButton:hover{
background-color:rgba(2,65,118,150);
color:rgba(255,255,255,200);
border-radius:5px;
}
QPushButton#pushButton:pressed{
padding-left:5px;
padding-top:5px;
background-color:rgba(2,65,118,100);
}

4 
隐藏框：
MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)

5
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
```

