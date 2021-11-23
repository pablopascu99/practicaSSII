from main_window import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, app, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.app = app

if __name__ == "__main__":
    global app
    app = QtWidgets.QApplication([])
    window = MainWindow(app)
    window.show()
    app.exec_()