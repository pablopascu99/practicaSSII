from main_window import *
from similarity_window import *
from PyQt5.QtWidgets import QFileDialog
import os

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow, similarity):
    def __init__(self, app, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.initSimilarity()
        self.setWindowIcon(QtGui.QIcon('./img/periodico.png'))
        self.setWindowTitle("Busquedas y recomendaciones")
        self.textos.setReadOnly(True)
        self.botonbuscar.clicked.connect(self.obtainText)
        self.app = app

    def obtainText (self):
        textos = []
        self.textNames = os.listdir(self.lineEdit_2.text())
        for n in self.textNames:
            file = open(self.lineEdit_2.text()+'/'+n, "r")
            textos.append(file.read())
        print(textos)
        '''
        texto = 'diario.txt'
        f = open(texto , 'r')
        text = f.read()
        print(text)
        f.close
        self.textEdit.setText(text)
        '''

    def abrirCarpeta(self):
        self.lineEdit_2.clear()
        dir = QFileDialog.getExistingDirectory(
            self, "Open directory", "/home", QFileDialog.ShowDirsOnly)
        if dir != "":
            self.lineEdit_2.clear()
            self.lineEdit_2.setText(dir)

if __name__ == "__main__":
    global app
    app = QtWidgets.QApplication([])
    window = MainWindow(app)
    window.show()
    app.exec_()