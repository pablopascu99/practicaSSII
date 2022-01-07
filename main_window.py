# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        MainWindow.setMinimumSize(QtCore.QSize(800, 500))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.search = QtWidgets.QWidget()
        self.search.setObjectName("search")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.search)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.groupBox = QtWidgets.QGroupBox(self.search)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.nranking = QtWidgets.QSpinBox(self.groupBox)
        self.nranking.setObjectName("nranking")
        self.horizontalLayout.addWidget(self.nranking)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_4.addWidget(self.comboBox)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)
        self.botonbuscar = QtWidgets.QPushButton(self.groupBox)
        self.botonbuscar.setObjectName("botonbuscar")
        self.horizontalLayout_3.addWidget(self.botonbuscar)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.filtros = QtWidgets.QTextEdit(self.groupBox)
        self.filtros.setMarkdown("")
        self.filtros.setObjectName("filtros")
        self.horizontalLayout_2.addWidget(self.filtros)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_11.addWidget(self.groupBox)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.search)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.ranking = QtWidgets.QTableView(self.search)
        self.ranking.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.ranking.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ranking.setAlternatingRowColors(True)
        self.ranking.setTextElideMode(QtCore.Qt.ElideNone)
        self.ranking.setObjectName("ranking")
        self.ranking.horizontalHeader().setCascadingSectionResizes(True)
        self.ranking.horizontalHeader().setDefaultSectionSize(200)
        self.ranking.horizontalHeader().setMinimumSectionSize(0)
        self.ranking.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_6.addWidget(self.ranking)
        self.horizontalLayout_20.addLayout(self.verticalLayout_6)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.label_4 = QtWidgets.QLabel(self.search)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.textos = QtWidgets.QTextEdit(self.search)
        self.textos.setObjectName("textos")
        self.verticalLayout_4.addWidget(self.textos)
        self.horizontalLayout_20.addLayout(self.verticalLayout_4)
        self.verticalLayout_11.addLayout(self.horizontalLayout_20)
        self.gridLayout_4.addLayout(self.verticalLayout_11, 0, 0, 1, 1)
        self.tabWidget.addTab(self.search, "")
        self.similarity = QtWidgets.QWidget()
        self.similarity.setObjectName("similarity")
        self.gridLayout = QtWidgets.QGridLayout(self.similarity)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.similarity)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lineTexto = QtWidgets.QLineEdit(self.similarity)
        self.lineTexto.setObjectName("lineTexto")
        self.horizontalLayout_7.addWidget(self.lineTexto)
        self.openNoticiaSim = QtWidgets.QPushButton(self.similarity)
        self.openNoticiaSim.setObjectName("openNoticiaSim")
        self.horizontalLayout_7.addWidget(self.openNoticiaSim)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem4)
        self.label_10 = QtWidgets.QLabel(self.similarity)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_13.addWidget(self.label_10)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.showNoticiaSim = QtWidgets.QTextEdit(self.similarity)
        self.showNoticiaSim.setObjectName("showNoticiaSim")
        self.verticalLayout.addWidget(self.showNoticiaSim)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.similarity)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.spinBox = QtWidgets.QSpinBox(self.similarity)
        self.spinBox.setMinimum(5)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_8.addWidget(self.spinBox)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)
        self.pushButton_2 = QtWidgets.QPushButton(self.similarity)
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_9.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem7)
        self.label_8 = QtWidgets.QLabel(self.similarity)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem8)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        self.tableView = QtWidgets.QTableView(self.similarity)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_7.addWidget(self.tableView)
        self.horizontalLayout_12.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem9)
        self.label_9 = QtWidgets.QLabel(self.similarity)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_11.addWidget(self.label_9)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem10)
        self.verticalLayout_8.addLayout(self.horizontalLayout_11)
        self.showNoticiaSim_2 = QtWidgets.QTextEdit(self.similarity)
        self.showNoticiaSim_2.setObjectName("showNoticiaSim_2")
        self.verticalLayout_8.addWidget(self.showNoticiaSim_2)
        self.horizontalLayout_12.addLayout(self.verticalLayout_8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.similarity, "")
        self.recom = QtWidgets.QWidget()
        self.recom.setObjectName("recom")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.recom)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(140, 80, 160, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_14.addWidget(self.lineEdit_3)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_14.addWidget(self.pushButton)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.recom)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(490, 100, 160, 101))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem11)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_15.addWidget(self.label_11)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem12)
        self.verticalLayout_3.addLayout(self.horizontalLayout_15)
        self.textEdit_2 = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_3.addWidget(self.textEdit_2)
        self.layoutWidget_2 = QtWidgets.QWidget(self.recom)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 350, 956, 273))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem13)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_17.addWidget(self.label_12)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem14)
        self.verticalLayout_9.addLayout(self.horizontalLayout_17)
        self.tableView_2 = QtWidgets.QTableView(self.layoutWidget_2)
        self.tableView_2.setObjectName("tableView_2")
        self.verticalLayout_9.addWidget(self.tableView_2)
        self.horizontalLayout_16.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem15)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_18.addWidget(self.label_13)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem16)
        self.verticalLayout_10.addLayout(self.horizontalLayout_18)
        self.showNoticiaSim_3 = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.showNoticiaSim_3.setObjectName("showNoticiaSim_3")
        self.verticalLayout_10.addWidget(self.showNoticiaSim_3)
        self.horizontalLayout_16.addLayout(self.verticalLayout_10)
        self.tabWidget.addTab(self.recom, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Opciones de búsqueda"))
        self.label.setText(_translate("MainWindow", "Número de resultados:"))
        self.label_5.setText(_translate("MainWindow", "Filtrar:"))
        self.botonbuscar.setText(_translate("MainWindow", "Buscar"))
        self.label_2.setText(_translate("MainWindow", "Realizar consulta:"))
        self.filtros.setPlaceholderText(_translate("MainWindow", "Escriba la consulta que desee realizar."))
        self.label_3.setText(_translate("MainWindow", "Ranking"))
        self.label_4.setText(_translate("MainWindow", "Noticia"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.search), _translate("MainWindow", "Búsqueda libre"))
        self.label_6.setText(_translate("MainWindow", "Selecciona la noticia que desee:"))
        self.openNoticiaSim.setText(_translate("MainWindow", "Abrir..."))
        self.label_10.setText(_translate("MainWindow", "Vista previa"))
        self.label_7.setText(_translate("MainWindow", "Numero de similitudes"))
        self.pushButton_2.setText(_translate("MainWindow", "Buscar similitudes"))
        self.label_8.setText(_translate("MainWindow", "Ranking"))
        self.label_9.setText(_translate("MainWindow", "Noticia"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.similarity), _translate("MainWindow", "Similitud a noticia"))
        self.pushButton.setText(_translate("MainWindow", "Abrir..."))
        self.label_11.setText(_translate("MainWindow", "Vista previa"))
        self.label_12.setText(_translate("MainWindow", "Ranking"))
        self.label_13.setText(_translate("MainWindow", "Noticia"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.recom), _translate("MainWindow", "Recomendación"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
