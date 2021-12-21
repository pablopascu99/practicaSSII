from PyQt5.QtWidgets import QFileDialog

class similarity():

    def initSimilarity(self):
        self.similarity = []
        self.lineTexto.setReadOnly(True)
        self.openNoticiaSim.clicked.connect(self.printsuma)

    def pruebaBoton(self):
        self.showNoticiaSim.setText("Holaaa")

    #Creamos una funcion para obtener el texto que desea el usuario para
    #posteriormente mostrarlo en la vista previa y realizar una busqueda 
    #de similitudes
    def getTextFile(self):
        self.lineTexto.clear()
        
        textName = QFileDialog.getOpenFileName(self, 'Open text file', '/home', "texto (*.txt)")
        if textName[0] != "":
            self.lineTexto.clear()
            self.lineTexto.setText(textName[0])
            self.showNoticiaSim.setText(textName[0])