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
        self.botonbuscar.clicked.connect(self.resultadoRanking)
        self.app = app

    def abrirCarpeta(self):
        self.lineEdit_2.clear()
        dir = QFileDialog.getExistingDirectory(
            self, "Open directory", "/home", QFileDialog.ShowDirsOnly)
        if dir != "":
            self.lineEdit_2.clear()
            self.lineEdit_2.setText(dir)

    def resultadoRanking(self):
        resultados = []

        #Obtenemos los valores de los diferentes filtros dados por el usuario
        #1.Filtrado por periodicos 2.Filtrado libre 3.Filtrado por numero de textos en el ranking
        listaBusqueda = localizar_directorio(self.comboBox.currentText())
        query = self.filtros.toPlainText()
        numranking = self.nranking.value()

        #Realizamos la similitud mediante el filtrado libre "ListaBusqueda"
        similitud = similitud_coseno(pathToNoticias(listaBusqueda, query)
            ,listaBusqueda).sort_values(axis=0,ascending=False)

        for fichero, similitud in similitud.items():
            listaResultados = []
            listaResultados.append(str(fichero))
            listaResultados.append(str(similitud))
            resultados.append(listaResultados)
        
        #Definimos el tamaño de la matriz
        numFilas = numranking
        numColumnas = 2

        #Establecemos las columnas y filas de nuestro widget tabla
        self.tableWidget.setRowCount(numFilas)
        self.tableWidget.setColumnCount(numColumnas)

        #Iteramos mediante dos for para ir imprimiendo la informacion en la widget
        for row in range (numFilas):
            for column in range (numColumnas):
                self.tableWidget.setItem(row, column, QTableWidgetItem((resultados[row][column])))
        
        #Establecemos un tamaño para la columna de los nombres de los archivos
        #para tener una mejor lectura de los mismos
        self.tableWidget.setColumnWidth(0,359)

    def rowSeleccionada(self):
        row = self.tableWidget.currentRow()
        item = self.tableWidget.item(row, 0)

        textoShow=""
        file = open(item.text(), "r", encoding='utf-8')
        textoShow += file.read()
        self.textos.setText(textoShow)

if __name__ == "__main__":
    global app
    app = QtWidgets.QApplication([])
    window = MainWindow(app)
    window.show()
    app.exec_()