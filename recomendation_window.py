from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QTableWidgetItem
from busqueda import *

class recomendation():

    def initRecomendation(self):
        self.recomendacion = []
        self.showNoticiaRec.setReadOnly(True)
        self.tableWidget_3.itemSelectionChanged.connect(self.rowSeleccionadaRec)
        self.realizarRecomendacion.clicked.connect(self.prueba)

    def prueba (self):
        categoria = self.comboCategoria.currentText()
        if categoria == "salud":
            print("Funciona")
        else:
            print("No funciona")

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