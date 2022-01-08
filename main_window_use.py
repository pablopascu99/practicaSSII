from main_window import *
from similarity_window import *
from busqueda import *
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QTableWidgetItem
import os
import pandas as pd

nltk.download('stopwords')

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow, similarity):
    def __init__(self, app, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.initSimilarity()
        self.setWindowIcon(QtGui.QIcon('./img/periodico.png'))
        self.setWindowTitle("Busquedas y recomendaciones")
        self.textos.setReadOnly(True)
        self.botonbuscar.clicked.connect(self.prueba)
        self.app = app

    def abrirCarpeta(self):
        self.lineEdit_2.clear()
        dir = QFileDialog.getExistingDirectory(
            self, "Open directory", "/home", QFileDialog.ShowDirsOnly)
        if dir != "":
            self.lineEdit_2.clear()
            self.lineEdit_2.setText(dir)
    
    #OBTENER EL UMERO DE RESULTASDOS QUE QUEREMOS DEL SPINBOX
    #OBTENER EL UMERO DE RESULTASDOS QUE QUEREMOS DEL IFLTRAOD DE PERIODicos
    #PONER NOMBRE A LAS COLUMNAS
    
    def prueba(self):
        #print(localizar_directorio(self.comboBox.currentText()))
        listaBusqueda = localizar_directorio(self.comboBox.currentText())
        resultados = []

        query = self.filtros.toPlainText()

        similitud = similitud_coseno(pathToNoticias(listaBusqueda, query)
            ,listaBusqueda).sort_values(axis=0,ascending=False)

        for fichero, similitud in similitud.items():
            daigual = []
            daigual.append(str(fichero))
            daigual.append(str(similitud))
            resultados.append(daigual)
        
        #Definimos el tama;o de la matriz
        numFilas = 5
        numColumnas = 2

        #COMENTAR ESTODFJLOKWNIOFHNW
        self.tableWidget.setRowCount(numFilas)
        self.tableWidget.setColumnCount(numColumnas)

        # Loops to add values into QTableWidget
        for row in range (numFilas):
            for column in range (numColumnas):
                self.tableWidget.setItem(row, column, QTableWidgetItem((resultados[row][column])))



        
        

if __name__ == "__main__":
    global app
    app = QtWidgets.QApplication([])
    window = MainWindow(app)
    window.show()
    app.exec_()