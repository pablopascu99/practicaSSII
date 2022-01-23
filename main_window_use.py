from main_window import *
from similarity_window import *
from recomendation_window import *
from busqueda import *
from PyQt5.QtWidgets import QTableWidgetItem

nltk.download('stopwords')

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow, similarity, recomendation):
    def __init__(self, app, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        #Iniciamos las dos ventanas complementarias
        self.initSimilarity()
        self.initRecomendation()
        #Establecemos tanto un logo como título del programa
        self.setWindowIcon(QtGui.QIcon('./img/periodico.png'))
        self.setWindowTitle("Busquedas y recomendaciones")
        #Establecemos la propiedad de solo lectura al componente textos
        self.textos.setReadOnly(True)
        #Establecemos la funcion a ejecutar cuando se clicke en los botones
        self.botonbuscar.clicked.connect(self.resultadoRanking)
        self.tableWidget.itemSelectionChanged.connect(self.rowSeleccionada)
        self.app = app

    #Funcion para realizar la similitud respecto a busqueda libre
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
        resultados.pop(0)
        
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

    #Funcion dedicada a la visualizacion de elementos del ranking
    def rowSeleccionada(self):
        #Introducimos la noticia clickada en "item"
        row = self.tableWidget.currentRow()
        item = self.tableWidget.item(row, 0)

        #Obtenemos el texto del item seleccionado
        textoShow=""
        file = open(item.text(), "r", encoding='utf-8')
        textoShow += file.read()
        #Imprimimos el texto en el espacio de "Noticia"
        self.textos.setText(textoShow)

if __name__ == "__main__":
    global app
    app = QtWidgets.QApplication([])
    window = MainWindow(app)
    window.show()
    app.exec_()