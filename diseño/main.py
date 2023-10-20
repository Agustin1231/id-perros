from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QGraphicsDropShadowEffect
from PyQt5.QtCore import QFile, QTextStream
from PyQt5 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import (QIcon)

import sys

from SqMain import Ui_MainWindow
from SqTamano import Ui_Form

class ventanaApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("ID Perros")
        self.titulo.setText("Escoge a tu perro ideal")
        self.tituloCompatibilidad.setText("Proximo amigo")
        self.btnTam.setText("Tamaño")
        self.btnActividad.setText("Actividad Fisica")
        self.btnCaracter.setText("Caracter")
        self.btnClima.setText("Clima")

        self.btnTam.clicked.connect(self.mostrarTam)
    
    def mostrarTam(self):
        window.hide()
        tam.show()


class ventanaTam(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        self.tituloTam.setText("TAMAÑO")
        self.pregTam.setText("¿Prefieres perros pequeños, medianos o grandes?")
        self.boxTam.addItems(["Pequeños", "Medianos", "Grandes"])
        self.aceptar.clicked.connect(self.obtenerInformacion)

    def obtenerInformacion(self):
        print("Degree : {0}".format(self.boxTam.currentText()))
        tam.hide()
        window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(open("./diseño/style.css", "r").read())
    tam = ventanaTam()
    window = ventanaApp()
    window.show()
    sys.exit(app.exec())