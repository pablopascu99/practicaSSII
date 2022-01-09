from PyQt5.QtWidgets import QFileDialog
import os

class similarity():

    def initSimilarity(self):
        self.similarity = []
        self.lineTexto.setReadOnly(True)
        self.showNoticiaSim.setReadOnly(True)
        self.showNoticiaSim_2.setReadOnly(True)
        self.openNoticiaSim.clicked.connect(self.getTextDirText)

    def getTextDirText(self):
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
    
