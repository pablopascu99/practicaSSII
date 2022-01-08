from PyQt5.QtWidgets import QFileDialog
import os

class similarity():

    def initSimilarity(self):
        self.similarity = []
        self.lineTexto.setReadOnly(True)
        self.showNoticiaSim.setReadOnly(True)
        self.showNoticiaSim_2.setReadOnly(True)
        self.openNoticiaSim.clicked.connect(self.getTextDirText)

    #Creamos una funcion para obtener el texto que desea el usuario para
    
    #posteriormente mostrarlo en la vista previa y realizar una busqueda 
    #de similitudes
    def getTextDirText(self):
        self.lineTexto.clear()
        
        textName = QFileDialog.getOpenFileName(self, 'Open text file', '/home', "texto (*.txt)")
        if textName[0] != "":
            self.lineTexto.clear()
            self.lineTexto.setText(textName[0])
            textoShow = ""
            file = open(textName[0], "r")
            textoShow += file.read()
            self.showNoticiaSim.setText(textoShow)
    
