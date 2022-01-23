from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QTableWidgetItem
from busqueda import *

class recomendation():

    '''
    Funcion que determina la incializacion de la ventana y sus componentes
    ''' 
    def initRecomendation(self):
        self.recomendacion = []
        self.showNoticiaRec.setReadOnly(True)
        self.tableWidget_3.itemSelectionChanged.connect(self.rowSeleccionadaRec)
        self.realizarRecomendacion.clicked.connect(self.recomendacionTexto)

    def recomendacionTexto(self):
        #Borramos lo que hubiera escrito anteriormente en la direccion
        self.lineTexto_2.clear()
        #Abrimos una ventana emergente para abrir el archivo de texto deseado
        textName = QFileDialog.getOpenFileName(self, 'Open text file', '/home', "texto (*.txt)")

        #Mostramos la direccion del archivo de texto abierto y imprimimos el texto del txt
        if textName[0] != "":
            self.lineTexto_2.clear()
            self.lineTexto_2.setText(textName[0])
            textoShow = ""
            file = open(textName[0], "r", encoding='utf-8')
            textoShow += file.read()
            self.showNoticiaRec.setText(textoShow)

        resultados = []

        #Obtenemos los valores de los diferentes filtros dados por el usuario
        #1.Filtrado por periodicos 2.Filtrado libre 3.Filtrado por numero de textos en el ranking
        listaBusqueda = localizar_directorio(self.comboBox_4.currentText())
        textoPred = textName[0]
        numranking = self.nranking_3.value()

        query_root = open(textoPred, 'r', encoding="utf-8")
        query = query_root.read()
        query_root.close()

        #Realizamos la recomendacion mediante sorensen, introduciendo la query y la carpeta a comparar
        sorensen = calculo_sorensen_dice_path(listaBusqueda, query).sort_values(by='sd',axis=0,ascending=False)
        
        for fichero, sorensen in sorensen.items():
            listaResultados = []
            listaResultados.append(str(fichero))
            listaResultados.append(str(sorensen))
            resultados.append(listaResultados)
    
        #Definimos el tamaño de la matriz
        numFilas = numranking
        numColumnas = 2

        #Establecemos las columnas y filas de nuestro widget tabla
        self.tableWidget_3.setRowCount(numFilas)
        self.tableWidget_3.setColumnCount(numColumnas)

        #Iteramos mediante dos for para ir imprimiendo la informacion en la widget
        for row in range (numFilas):
            for column in range (numColumnas):
                self.tableWidget_3.setItem(row, column, QTableWidgetItem((resultados[row][column])))

        #Establecemos un tamaño para la columna de los nombres de los archivos
        #para tener una mejor lectura de los mismos
        self.tableWidget_3.setColumnWidth(0,316)
        self.tableWidget_3.setColumnWidth(1,140)

    #Creacion de funcion para la seleccion de las noticias mostadas en el ranking
    def rowSeleccionadaRec(self):
        #Se obiene la columna seleccionada como "item"
        row = self.tableWidget_3.currentRow()
        item = self.tableWidget_3.item(row, 0)

        #Obtenemos el texto del item seleccionado.
        textoShow=""
        file = open(item.text(), "r", encoding='utf-8')
        textoShow += file.read()
        #Imprimimos el texto en el espacio de "Noticia"
        self.showNoticiaSim_3.setText(textoShow)
        #pyuic5 -x window.ui -o main_window.py