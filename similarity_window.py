from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QTableWidgetItem
from busqueda import *
import os

class similarity():

    def initSimilarity(self):
        self.similarity = []
        self.lineTexto.setReadOnly(True)
        self.showNoticiaSim.setReadOnly(True)
        self.showNoticiaSim_2.setReadOnly(True)
        self.openNoticiaSim.clicked.connect(self.similitudTexto)
        self.tableWidget_2.itemSelectionChanged.connect(self.rowSeleccionadaSim)

    def similitudTexto(self):
        #Borramos lo que hubiera escrito anteriormente en la direccion
        self.lineTexto.clear()
        #Abrimos una ventana emergente para abrir el archivo de texto deseado
        textName = QFileDialog.getOpenFileName(self, 'Open text file', '/home', "texto (*.txt)")

        #Mostramos la direccion del archivo de texto abierto y imprimimos el texto del txt
        if textName[0] != "":
            self.lineTexto.clear()
            self.lineTexto.setText(textName[0])
            textoShow = ""
            file = open(textName[0], "r", encoding='utf-8')
            textoShow += file.read()
            self.showNoticiaSim.setText(textoShow)

        resultados = []

        #Obtenemos los valores de los diferentes filtros dados por el usuario
        #1.Filtrado por periodicos 2.Filtrado libre 3.Filtrado por numero de textos en el ranking
        listaBusqueda = localizar_directorio(self.comboBox_2.currentText())
        query = textName[0]
        numranking = self.nranking_2.value()

        #Realizamos la similitud mediante el filtrado libre "ListaBusqueda"
        similitud = similitud_coseno(pathToNoticias2(listaBusqueda, query)
            ,listaBusqueda).sort_values(axis=0,ascending=False)

        for fichero, similitud in similitud.items():
            listaResultados = []
            listaResultados.append(str(fichero))
            listaResultados.append(str(similitud))
            resultados.append(listaResultados)
        resultados.pop(0)
        
        #Definimos el tamaño de la matriz
        numFilas = numranking
        numColumnas = 2

        #Establecemos las columnas y filas de nuestro widget tabla
        self.tableWidget_2.setRowCount(numFilas)
        self.tableWidget_2.setColumnCount(numColumnas)

        #Iteramos mediante dos for para ir imprimiendo la informacion en la widget
        for row in range (numFilas):
            for column in range (numColumnas):
                self.tableWidget_2.setItem(row, column, QTableWidgetItem((resultados[row][column])))

        #Establecemos un tamaño para la columna de los nombres de los archivos
        #para tener una mejor lectura de los mismos
        self.tableWidget_2.setColumnWidth(0,316)
        self.tableWidget_2.setColumnWidth(1,140)

    def rowSeleccionadaSim(self):
        row = self.tableWidget_2.currentRow()
        item = self.tableWidget_2.item(row, 0)

        textoShow=""
        file = open(item.text(), "r", encoding='utf-8')
        textoShow += file.read()
        self.showNoticiaSim_2.setText(textoShow)


        


        



